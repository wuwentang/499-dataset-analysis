import pyspark
import pandas as pd
import pyspark.sql.functions as func
from pyspark.sql import Row
from pyspark.ml.fpm import FPGrowth
from pyspark.sql import SparkSession


spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# remove duplicate restaurants
def remove_duplicate(x):
    x.drop_duplicates(keep=False, inplace=True)
    return x.tolist()

df = pd.read_csv('data/test_data_review_businesses.csv')

user_business_df = df[['user_id', 'business_id']]

# group user_id with list of business_id
user_id_df = user_business_df.groupby('user_id').agg(lambda x: remove_duplicate(x))
print(user_id_df)

# convert pandas df to spark df
user_id_df = spark.createDataFrame(user_id_df.astype(list))

user_id_df.show()
# Python API docs
fpGrowth = FPGrowth(itemsCol="business_id", minSupport=0.5, minConfidence=0.6)
model = fpGrowth.fit(user_id_df)

# Display frequent itemsets
model.freqItemsets.show(20, truncate=False)

