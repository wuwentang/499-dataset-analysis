from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.feature import StringIndexer
from pyspark.ml import Pipeline
from pyspark.sql.types import IntegerType

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark.read.csv('data/test_data_review_businesses.csv', header=True)
#selecting useful columns
nd = df.select(df['business_id'],df['stars'],df['user_id'])

#converting string to index
indexer = [StringIndexer(inputCol=column, outputCol=column+"_index") for column in list(set(nd.columns)-set(['stars']))]
pipeline = Pipeline(stages=indexer)
transformed = pipeline.fit(nd).transform(nd)

transformed = transformed.withColumn('stars', transformed['stars'].cast(IntegerType()))

#creating training and test set
(training,test) = transformed.randomSplit([0.8, 0.2])

#need to find best values for maxiter, regparam and rank
als = ALS(maxIter=5,regParam=0.01,rank=25,
          userCol="user_id_index",itemCol="business_id_index",ratingCol="stars",
          coldStartStrategy="drop",nonnegative=True)
model = als.fit(training)

evaluator = RegressionEvaluator(metricName="rmse",labelCol="stars",predictionCol="prediction")

predictions = model.transform(test)
rmse = evaluator.evaluate(predictions)
print(str(rmse))

recommendations = model.recommendForAllUsers(20).show(10)
