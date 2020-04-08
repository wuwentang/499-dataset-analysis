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

df = spark.read.csv('data/test_data_review_businesses.csv', header=True)

user_business_df = df.select(df['user_id'], df['business_id'])
print(user_business_df.show())

user_id_df = user_business_df.groupby(func.col("user_id")).agg(lambda x: x.tolist())
print(user_id_df.show())

# Python API docs
fpGrowth = FPGrowth(itemsCol="business_id", minSupport=0.5, minConfidence=0.6)
model = fpGrowth.fit(user_id_df)

# Display frequent itemsets
model.freqItemsets.show()

