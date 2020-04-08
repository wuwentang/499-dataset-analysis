from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.feature import StringIndexer
from pyspark.ml import Pipeline
from pyspark.sql.types import IntegerType
import pandas as pd

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark.read.csv('data/test_data_review_businesses.csv', header=True)
#selecting useful columns
nd = df.select(df['business_id'],df['review_stars'],df['user_id'])

#converting string to index
indexer = [StringIndexer(inputCol=column, outputCol=column+"_index") for column in list(set(nd.columns)-set(['review_stars']))]
pipeline = Pipeline(stages=indexer)
transformed = pipeline.fit(nd).transform(nd)

transformed = transformed.withColumn('review_stars', transformed['review_stars'].cast(IntegerType()))

#creating training and test set
(training,test) = transformed.randomSplit([0.8, 0.2])

#need to find best values for maxiter, regparam and rank
als = ALS(maxIter=5,regParam=0.01,rank=25,
          userCol="user_id_index",itemCol="business_id_index",ratingCol="review_stars",
          coldStartStrategy="drop",nonnegative=True)
model = als.fit(training)

evaluator = RegressionEvaluator(metricName="rmse",labelCol="stars",predictionCol="prediction")

predictions = model.transform(test)
rmse = evaluator.evaluate(predictions)
print(str(rmse))

recommendations = model.recommendForAllUsers(20).toPandas()

#taking out the indexes to see recommendations in terms of business id
recs = model.recommendForAllUsers(10).toPandas()
nrecs = recs.recommendations.apply(pd.Series) \
            .merge(recs, right_index=True, left_index=True) \
            .drop(["recommendations"], axis=1) \
            .melt(id_vars=['user_id_index'], value_name="recommendation") \
            .drop("variable", axis=1) \
            .dropna()

nrecs = nrecs.sort_values('user_id_index')
nrecs = pd.concat([nrecs['recommendation'].apply(pd.Series), nrecs['user_id_index']], axis=1)
nrecs.columns = [

    'ProductID_index',
    'Rating',
    'UserID_index'

]

md = transformed.select(transformed['user_id'],transformed['user_id_index'],
                        transformed['business_id'],transformed['business_id_index'])
md = md.toPandas()
dict1 = dict(zip(md['user_id_index'],md['user_id']))
dict2 = dict(zip(md['business_id_index'],md['business_id']))
nrecs['user_id']=nrecs['UserID_index'].map(dict1)
nrecs['business_id']=nrecs['ProductID_index'].map(dict2)
nrecs = nrecs.sort_values('user_id')
new = nrecs[['user_id','business_id','Rating']]
new['recommendations'] = list(zip(new.business_id, new.Rating))
res = new[['user_id','recommendations']]
res_new = res['recommendations'].groupby([res.user_id]).apply(list).reset_index()

print(res_new)
