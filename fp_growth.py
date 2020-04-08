import pyspark
import pandas as pd
import pyspark.sql.functions as func
from pyspark.sql import Row
from pyspark.ml.fpm import FPGrowth
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

rdd = spark.sparkContext.textFile('data/test_data_review_businesses.csv')

# removing header
header = rdd.first()

# filter header out and create user_id -> business_id rdd
data_rdd = rdd.filter(lambda row: row != header).map(lambda row: Row(business_id=row.split(",")[0], user_id=row.split(",")[5]))

# remove duplicate rows
data_rdd = data_rdd.map(lambda row: row).distinct()

# create DataFrame
data_df = spark.createDataFrame(data_rdd)
data_df = data_df.groupby('user_id').agg(F.collect_list('business_id'))

# # Python API docs
fpGrowth = FPGrowth(itemsCol="collect_list(business_id)", minSupport=0.5, minConfidence=0.6)

# # model = spark.sparkContext.parallelize(fpGrowth.fit(user_id_df), numSlices=1000)
model = fpGrowth.fit(data_df)

# # Display frequent itemsets
model.freqItemsets.show(20, truncate=False)

