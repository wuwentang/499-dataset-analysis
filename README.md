# 499-dataset-analysis

## Team members

- Wu Wen Tang (ID 40028075)
- Zhen Yee (ID 40028478)
- Razvan Soos (ID 40035034)

## Abstract
This project is a dataset analysis of the [Yelp dataset](https://www.yelp.com/dataset), available to the public as JSON files. We will apply two techniques seen in the course using Apache Spark, Dask or scikit-learn. The results will be discussed and interpreted.

The Yelp dataset is a subset of businesses, reviews and user data, written on the yelp review website, designed to be used for personal or educational purposes. There are multiple ways of using the Yelp dataset, including predicting restaurant [closure](https://towardsdatascience.com/using-yelp-data-to-predict-restaurant-closure-8aafa4f72ad6), popularity, etc. based on various factors such as restaurant density, review count, rating, and price relative to surrounding restaurants. Additionally, the yelp dataset provides user information, reviews or tips users left to businesses which can be used to study a pattern between users and pictures of the food, drinks, menu or restaurant which can be used for image classification.

## Introduction
It has been noticed that restaurants can have great or not so great success partially depending on the location where they open and that different restaurants have a broad type of reviews, whether positive or negative also partially depending on their location. Our hypothesis is that a restaurant is far more likely to have negative reviews and eventually fail given that it’s located in the wrong neighbourhood for its type. In other words, we're formulating an association rule between neighbourhood, restaurant types, and the review "stars" range. E.g. {neighborhood, restaurant type, (other types/features)} => review range 1-5*

The objective of this research is to determine the positive or negative impact that the location of a restaurant has given the type of the restaurant. In other words we’re interested in seeing whether or not, for example, an Italian restaurant will succeed better in an Italian neighbourhood compared to an Italian restaurant located in Chinatown or downtown. This will be done by studying the reviews of successful and now closed restaurants in different parts of town for multiple major cities such as Montreal, Toronto or New York. Another thing to consider would be if the location of the restaurant is near famous landmarks, schools, malls, parks, or other public infrastructures. We believe that would have influence on the success as well. A significant problem in this research is that tesides the reviews, additional data has to be taken into account and reasonably standardized, notably the fame of the restaurant itself and the fame of the chefs cooking there. What we mean by this is that a Gordon Ramsey Italian restaurant that opens near Chinatown could see far more success than any other Italian restaurant located near Chinatown and more than likely even some Italian restaurants open in Little Italy. Comparing restaurants owned by well known chefs or large franchises to a family owned restaurant whose owners have little to no experience in running a restaurant business won’t make for accurate data, therefore a scale for comparison between big names or between new owners will need to be created at first.

In regards to the related work, there have been hundreds of academic papers written using the Yelp dataset as well as many more projects made on the analysis of the dataset.

## Materials & Methods
### Datasets
The datasets used are the Yelp Open dataset, and the Ward Profiles, 2018 (47-Ward Model), available from City Planning through the online Toronto Data, Research & Maps portal. There is an API available to extract the data from the Ward dataset.

The _Yelp dataset_ contains many attributes such as hours, parking, availability, ambience, etc. It also contains full review text data including user_id that wrote the review, the business_id the review is written for, date, etc. It is around 8GB. The information that is interesting to us in the scope of this project is the following:
- business "categories" ("Mexican", "Burgers", "Gastropubs")
- "postal code": "94107",
- "Latitude"
- "longitude": -122.39612197,
- "stars": 4.5,
- "review_count": 1198,

The _2016 Ward profiles_ contain information on population by “age; households and dwelling types; families; language group; household tenure and period of construction; immigration and mobility; ethnic origin and visible minorities; education and labour force; income and shelter cost”. The information that is interesting to us in the scope of this project is the following:
Migration, Mobility, and Languages
- Area name
- Latitude
- Longitude 

### Technologies
The technologies that will be used are Apache Spark, and scikit-learn.

_Apache Spark_

Apache Spark is built around RDDs, a dataset distributed over a cluster of machines. It was developed to overcome the limitations of MapReduce cluster computing model; and extends the model. Spark is more efficient in both iterative algorithms, and exploratory data analysis (e.g. the repeated database-style querying of data). Spark has in-memory cluster computing, which increases the processing speed of an application. Spark automatically distributes the data in RDDs across clusters and parallelizes the data.

_Scikit-learn_

Scikit-learn is a machine learning library for Python. It has classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN. Scikit-learn integrates with other Python libraries: matplotlib and plotly for plotting, numpy for array vectorization, pandas dataframes, scipy, etc. 

### Algorithms
_K-means Clustering_

k-means clustering is a machine learning algorithm, used in data science for cluster analysis. The goal of K-means to group similar data points together to find patterns; K-means looks for a number (k) of clusters in a dataset, which is a collection of data points aggregated by similarities.

In our case, k-means clustering will be used to separate types of restaurants, for example, family owned restaurants or chain restaurants. They will be separated, similar categories grouped together and compared. Similarly, certain ethnicity groups will also be separated in this way, but more thoughts will be put behind that later.

_Nearest neighbours_

The k-nearest neighbors (KNN) algorithm is a supervised machine learning algorithm, used to solve both classification and regression problems. This algorithm relies on labeled input data to learn a function that will be able to produce a correct output when given new unlabeled data; it assumes that similar things exist near each other.

We want to be able to identify new restaurants based on this algorithm.


## References
https://open.toronto.ca/dataset/ward-profiles-2018-47-ward-model/

https://en.wikipedia.org/wiki/Apache_Spark

https://en.wikipedia.org/wiki/Scikit-learn

https://en.wikipedia.org/wiki/K-means_clustering#Algorithms

https://towardsdatascience.com/understanding-k-means-clustering-in-machine-learning-6a6e67336aa1

https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761

