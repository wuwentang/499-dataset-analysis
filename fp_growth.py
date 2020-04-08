import pyspark
import pandas as pd
import pyspark.sql.functions as func
from pyspark.sql import Row
from pyspark.ml.fpm import FPGrowth
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import array_distinct

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# rdd = spark.sparkContext.textFile('data/test_data_review_businesses.csv')
rdd = spark.sparkContext.textFile('data/yelp_reviews_businesses.csv')

# removing header
header = rdd.first()

# filter header out and create user_id -> business_id rdd
data_rdd = rdd.filter(lambda row: row != header).map(lambda row: Row(business_id=row.split(",")[0], user_id=row.split(",")[5]))

# remove duplicate rows
data_rdd = data_rdd.map(lambda row: row).distinct()

# create DataFrame
data_df = spark.createDataFrame(data_rdd)
data_df = data_df.groupby('user_id').agg(F.collect_list('business_id'))

# group restaurants with same name but different location together
data_df = data_df.withColumn("business_id_list", array_distinct("collect_list(business_id)"))

# # Python API docs
fpGrowth = FPGrowth(itemsCol="business_id_list", minSupport=0.001, minConfidence=0.5)
model = fpGrowth.fit(data_df)

# # Display frequent itemsets
model.freqItemsets.orderBy([func.size("items"), "freq"], ascending=[0, 0]).show(20, truncate=False)

# Association Rules
association = model.associationRules
association.orderBy([func.size("antecedent"), "confidence"], ascending=[0,0]).show(20, truncate=False)

transform = model.transform(data_df)
transform = transform.drop("collect_list(business_id)")
transform.orderBy([func.size("prediction")], ascending=[0,0]).show(20, truncate=False)
