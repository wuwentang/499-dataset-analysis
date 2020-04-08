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

# remove duplicate restaurants
def remove_duplicate(x):
    x.drop_duplicates(keep=False, inplace=True)
    return x.tolist()

# df = pd.read_csv('data/test_data_review_businesses.csv')

# user_business_df = df[['user_id', 'business_id']]

# # group user_id with list of business_id
# user_id_df = user_business_df.groupby('user_id').agg(lambda x: remove_duplicate(x))
# print(user_id_df)


# # convert pandas df to spark df
# user_id_dff = spark.createDataFrame(user_id_df)

rdd = spark.sparkContext.textFile('data/test_data_review_businesses.csv')
header = rdd.first()
data_rdd = rdd.filter(lambda row: row != header).map(lambda row: Row(business_id=row.split(",")[0], user_id=row.split(",")[5]))
data_df = spark.createDataFrame(data_rdd)
data_df = data_df[["user_id", "business_id"]]
data_df = data_df.groupby('user_id').agg(F.collect_list('business_id'))

data_df.show(20, truncate=False)

# user_id_dff.show(20, truncate=False)
# # Python API docs
# fpGrowth = FPGrowth(itemsCol="business_id", minSupport=0.5, minConfidence=0.6)

# # model = spark.sparkContext.parallelize(fpGrowth.fit(user_id_df), numSlices=1000)
# model = fpGrowth.fit(user_id_df)

# # Display frequent itemsets
# model.freqItemsets.show(20, truncate=False)

