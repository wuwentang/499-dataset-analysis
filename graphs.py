import pandas as pd
import numpy as np
import warnings
import matplotlib.pyplot as plt

df = pd.read_csv('data/yelp_reviews_businesses.csv', sep=',')
df1 = df[['business_id','stars']]
df1 = df.drop_duplicates()
df1.plot.hist(by='stars', bins=15)

df2 = df[['review_stars']]
df2.plot.hist(bins=15)
plt.show()
