import pandas as pd
# Reading the json file
business_json_path = 'data/yelp_academic_dataset_business.json'
df_b = pd.read_json(business_json_path, lines=True)
# Removing closed restaurants
df_b = df_b[df_b['is_open']==1]
# Keeping restaurants with more than 5 reviews
df_b = df_b[df_b['review_count']>=5]
# Removing data that isn't categorized as food,restaurants,fast food or bars
df_b = df_b[df_b['categories'].str.contains(
              'Food|Fast Food|Bars|Restaurants',
              case=False, na=False)]
# Keeping business_id, name, city, stars
drop_columns = ['hours','is_open','review_count','address','state','latitude','longitude', 'categories','attributes', 'postal_code']
df_b = df_b.drop(drop_columns, axis=1)

# Keeping only the toronto businesses
business_toronto = df_b[df_b['city']=="Toronto"]

review_json_path = 'data/yelp_academic_dataset_review.json'
size = 1000000
# Reading in chunks of 1 million to speed things up and identifying datatypes of each column to speed things up
review = pd.read_json(review_json_path, lines=True,
                      dtype={'review_id':str,'user_id':str,
                             'business_id':str,'stars':int,
                             'date':str,'text':str,'useful':int,
                             'funny':int,'cool':int},
                      chunksize=size)

# List of chunks to be read
chunk_list = []
for chunk_review in review:
    # Drop columns that aren't needed, keep user_id and stars
    chunk_review = chunk_review.drop(['review_id','useful','funny','cool','date','text'], axis=1)
    # Renaming column name to avoid conflict with business overall star rating
    chunk_review = chunk_review.rename(columns={'stars': 'review_stars'})
    # Inner merge with edited business file so only reviews related to the business remain
    chunk_merged = pd.merge(business_toronto, chunk_review, on='business_id', how='inner')
    print("step done") # Printing progress and allows me to see the total number of lines
    chunk_list.append(chunk_merged)
# After trimming down the review file, concatenate all relevant data back to one dataframe
df = pd.concat(chunk_list, ignore_index=True, join='outer', axis=0)
# Writing to csv file
csv_name = "data/yelp_reviews_businesses.csv"
df.to_csv(csv_name, index=False)