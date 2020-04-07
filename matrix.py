import pandas as pd

df = pd.read_csv('data/yelp_reviews_businesses.csv', sep=',')
#creating matrix with every row being a business and every column being an user. The value is the review number
matrix = df.pivot_table(index='user_id', columns='business_id', values='review_stars')
