# 499-dataset-analysis

## Team members

- Wu Wen Tang (ID 40028075)
- Zhen Yee (ID 40028478)
- Razvan Soos (ID 40035034)

## Abstract
This project is a dataset analysis of the [Yelp dataset](https://www.yelp.com/dataset), available to the public as JSON files. We will apply two techniques seen in the course using Apache Spark, Dask or scikit-learn. The results will be discussed and interpreted.

The Yelp dataset is a subset of businesses, reviews and user data, written on the yelp review website, designed to be used for personal or educational purposes. There are multiple ways of using the Yelp dataset, including predicting restaurant [closure](https://towardsdatascience.com/using-yelp-data-to-predict-restaurant-closure-8aafa4f72ad6), popularity, etc. based on various factors such as restaurant density, review count, rating, and price relative to surrounding restaurants. Additionally, the yelp dataset provides user information, reviews or tips users left to businesses which can be used to study a pattern between users and pictures of the food, drinks, menu or restaurant which can be used for image classification.

## I. Introduction
A recommender system is an algorithm that provides relevant information to a given user by finding patterns or similarities in a dataset. The algorithm would rate the items and shows the user the items that they would rate highly. Some of the most famous examples of recommender systems are: Amazon, items are recommended to you that the algorithm deemed to be relevant, Spotify, which recommends relevant music to the user, or Netflix, which recommends certain movies based on user accounts. In class, we learned about content based and collaborative filtering recommender systems. This project will focus on collaborative filtering recommender systems, where the preference of a group of users is used to make recommendations to other users. An example of this would be recommending a restaurant to a user because their friend liked the restaurant. Therefore, user-user collaborative filtering is relevant to our project. The goal is to find a set of users whose ratings are similar to the given user's ratings, in order to be able to recommend restaurants to the given user. In other words, a restaurant will be recommended to a given user based on the fact that the same restaurant have been liked by other similar users.

The objective of this research is to build a recommender system based on user ratings of restaurants. In our research, when two users 1 and 2 go to the same restaurants A and B, the similarity index of these two users is computed. Then, depending on the score, the system can recommend restaurant C to user 2 because these two users are similar in terms of the restaurants they visit. 

In regards to the related work, there are many other projects using the Yelp dataset, papers written using the Yelp dataset, as well as other projects made on the analysis of the dataset. Some examples are discussed below:

[Yelp recommendation](https://github.com/chanship/yelpRecommendation): Data mining is done with the Yelp dataset. They found the frequent itemsets in subsets of the Yelp dataset. They used Jaccard Similarity to identify similar user and business set. Then, they predicted the ratings/stars for the given user ids and business ids, an example of applying user-based collaborative filtering. 

This project looks very similar to ours, they apply many of the algorithms that we learned in class, as well as a few that we have not heard about. 

[SON implementation](https://github.com/manjar-cs/SON_Implementation): The SON algorithm (performs the Apriori algorithm) is implemented using the Apache Spark Framework. The goal of this project is to find frequent itemsets in two datasets: one simulated dataset(small1.csv,small2.csv), and one real-world dataset (generated from Yelp dataset). They want to apply the algorithm on large datasets more efficiently in a distributed environment.

This project is less relevant to our project, but still interesting because you can check how they convert the Yelp data. We will be converting the Yelp data from JSON to csv using pandas.

## II. Materials & Methods
### Dataset
The dataset used is the Yelp Open dataset. There are APIs available to extract the data from this dataset. This [website](https://www.kaggle.com/yelp-dataset/yelp-dataset/version/6#yelp_business_attributes.csv) gives a lot of information on the Yelp dataset. It's a great resource to view the information available.

The _Yelp dataset_ contains many attributes such as hours, parking, availability, ambience, etc. It also contains full review text data including user_id that wrote the review, the business_id the review is written for, date, etc. It is around 10GB. The information that is interesting to us in the scope of this project is in the following JSON files:
- yelp_academic_dataset_business.json
- yelp_academic_dataset_review.json
- yelp_academic_dataset_user.json
The other files will be disregarded. 


### Technologies
The technologies that will be used are Apache Spark, and scikit-learn.

_Apache Spark_

Apache Spark is built around RDDs, a dataset distributed over a cluster of machines. It was developed to overcome the limitations of MapReduce cluster computing model; and extends the model. Spark is more efficient in both iterative algorithms, and exploratory data analysis (e.g. the repeated database-style querying of data). Spark has in-memory cluster computing, which increases the processing speed of an application. Spark automatically distributes the data in RDDs across clusters and parallelizes the data.

_Scikit-learn_

Scikit-learn is a machine learning library for Python. It has classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN. Scikit-learn integrates with other Python libraries: matplotlib and plotly for plotting, numpy for array vectorization, pandas dataframes, scipy, etc. 

### Algorithms
_Frequent Itemsets_

The goal of frequent itemsets is to find sets of items that appear frequently together in "baskets". Frequent itemsets are generated by a set of items that appear in a defined number of support threshold s. Frequent itemset mining leads to associations between items in large data sets. Once the frequent itemsets are generated, association rules can be formed in the format of {item A} => {item B}.

In our case, frequent itemsets will be used to find frequent itemsets of restaurants per user. This can be used to find users who have similar tastes in restaurants, in user-based collaborative filtering. For example, 
Items = {Boustan, Wienstein & Gavino's, Pho Lien, Amir, M4 Burritos}
Support threshold = 3
B1 = {B, W, P}, B2 = {B, A, M}, B3 = {A, M}, B4 = {B, P}, B5 = {B, P, A, M}, ...
Frequent itemsets: {B}, {P}, {M}, {B, P}, {A, M}


_Alternating least Square (ALS)_

Matrix factorization algorithm is used to solve issues with collaborative filtering recommenders such as popularity bias,  cold-start problem, and scalability issue when more data is added to the data set. In a user-item interaction matrix, the data is also often sparse. For collaborative filtering, matrix factorization algorithms decompose the user-item interaction matrix into two matrices that are lower in dimension: one for the users, and one for the items.

ALS is a matrix factorization algorithm and and is implemented in Spark. It is used for collaborative filtering with large data sets. In this project, it is applied because it scales well to large datasets and can solve the sparseness problem of the restaurants ratings data. [Here](https://towardsdatascience.com/prototyping-a-recommender-system-step-by-step-part-2-alternating-least-square-als-matrix-4a76c58714a1) is an example for implementing a minimum viable product (MVP) ALS recommender system.

## III. Results


## IV. Discussion


## V. Conclusion


## References
https://open.toronto.ca/dataset/ward-profiles-2018-47-ward-model/

https://en.wikipedia.org/wiki/Apache_Spark

https://en.wikipedia.org/wiki/Scikit-learn

https://en.wikipedia.org/wiki/K-means_clustering#Algorithms

https://towardsdatascience.com/understanding-k-means-clustering-in-machine-learning-6a6e67336aa1

https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761

Edited:

https://towardsdatascience.com/how-to-build-a-simple-recommender-system-in-python-375093c3fb7d

https://towardsdatascience.com/prototyping-a-recommender-system-step-by-step-part-2-alternating-least-square-als-matrix-4a76c58714a1

https://www.sciencedirect.com/topics/computer-science/frequent-itemsets

https://www.edureka.co/blog/apriori-algorithm/#association-rules

https://github.com/chanship/yelpRecommendation

https://github.com/manjar-cs/SON_Implementation
