import pandas as pd

df = pd.read_csv('data/yelp_reviews_businesses.csv', sep=',')
#creating matrix with every row being a business and every column being an user. The value is the review number
user_item_matrix = df.pivot_table(index='user_id', columns='business_id', values='review_stars')

df1 = df[['business_id','name','stars']]
df1 = df1.drop_duplicates()
df1.sort_values(['stars'],ascending=False).head(10)

veghed_user_rating = user_item_matrix['VUADGMPLJoWqhHb1G4LIcA']
NOseafoodsteak = user_item_matrix['J9vAdD2dCpFuGsxPIn184w']

similar_to_veghed = user_item_matrix.corrwith(veghed_user_rating)
similar_to_NOseafoodsteak = user_item_matrix.corrwith(NOseafoodsteak)

corr_veghed= pd.DataFrame(similar_to_veghed, columns=['Correlation'])
corr_veghed.dropna(inplace=True)
corr_nosea = pd.DataFrame(similar_to_NOseafoodsteak,columns=['Correlation'])
corr_nosea.dropna(inplace=True)

print(corr_nosea)