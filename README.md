# 499-dataset-analysis

## Team members

- Wu Wen Tang (ID 40028075)
- Zhen Yee (ID 40028478)
- Razvan Soos (ID 40035034)




## Abstract
This project is a dataset analysis of the [Yelp dataset](https://www.yelp.com/dataset), available to the public as JSON files. We will apply two techniques seen in the course using Apache Spark, Dask or scikit-learn. The results will be discussed and interpreted.

The Yelp dataset is a subset of businesses, reviews and user data, written on the yelp review website, designed to be used for personal or educational purposes. There are multiple ways of using the Yelp dataset, including predicting restaurant [closure](https://towardsdatascience.com/using-yelp-data-to-predict-restaurant-closure-8aafa4f72ad6), popularity, etc. based on various factors such as restaurant density, review count, rating, and price relative to surrounding restaurants. Additionally, the yelp dataset provides user information, reviews or tips users left to businesses which can be used to study a pattern between users and pictures of the food, drinks, menu or restaurant which can be used for image classification.

## Introduction
It has been noticed that restaurants can have great or not so great success partially depending on the location where they open and that different restaurants have a broad type of reviews, whether positive or negative also partially depending on their location. Our hypothesis is that a restaurant is far more likely to have negative reviews and eventually fail given that it’s located in the wrong neighbourhood for its type.

The objective of this research is to determine the positive or negative impact that the location of a restaurant has given the type of the restaurant. In other words we’re interested in seeing whether or not, for example, an Italian restaurant will succeed better in an Italian neighbourhood compared to an Italian restaurant located in chinatown or downtown. This will be done by studying the reviews of successful and now closed restaurants in different parts of town for multiple major cities such as Montreal or New York. A significant problem in this research is that tesides the reviews, additional data has to be taken into account and reasonably standardized, notably the fame of the restaurant itself and the fame of the chefs cooking there. What we mean by this is that a Gordon Ramsey Italian restaurant that opens near chinatown could see far more success than any other Italian restaurant located near chinatown and more than likely even some Italian restaurants open in Little Italy. Comparing restaurants owned by well known chefs or large franchises to a family owned restaurant whose owners have little to no experience in running a restaurant business won’t make for accurate data, therefore a scale for comparison between big names or between new owners will need to be created at first.

In regards to the related work, there have been hundreds of academic papers written using the Yelp dataset as well as many more projects made on the analysis of the dataset.
