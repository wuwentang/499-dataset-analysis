import pandas as pd
import numpy as np
import warnings
import matplotlib.pyplot as plt

df = pd.read_csv('data/yelp_reviews_businesses.csv', sep=',')

df1 = df[['business_id','stars']]
df1 = df1.drop_duplicates()
df1.plot.hist(by='stars', bins=15)

df2 = df[['review_stars']]
df2.plot.hist(bins=15)

df3 = df[['business_id','user_id']]
df3 = df3.groupby("user_id").count()
df3 = df3.rename(columns={'business_id': 'Review Count'})
df3.plot.hist(bins=600)


df4 = df[['business_id','user_id']]
df4 = df4.groupby("user_id").count()
df4 = df4.rename(columns={'business_id': 'Review Count'})
df4 = df4.drop(df4[df4['Review Count'] > 100].index)
df4.plot.hist(bins=100)

df5 = df[['business_id','user_id']]
df5 = df5.groupby("user_id").count()
df5 = df5.rename(columns={'business_id': 'Review Count'})
df5 = df5.drop(df5[df5['Review Count'] > 20].index)
df5.plot.hist(bins=20)

plt.xticks(np.arange(1, 21, 1.0))
plt.show()
