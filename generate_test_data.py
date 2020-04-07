import pandas as pd
import random

training_data_path = 'data/yelp_reviews_businesses.csv'
df_business = pd.read_csv(training_data_path)

# Group reviews by user_id
df_group = df_business.groupby('user_id')

# Sample 0.4 of the reviews, so we can use them to predict ratings of rest of reviews
result = df_group.apply(lambda x: x.sample(frac=0.4, random_state=123))

# Output test data to csv file sorted by user_id
output_path = "data/test_data_review_businesses.csv"
result = result.sort_values('user_id')
result.to_csv(output_path, index=False)
