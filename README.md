# 499-dataset-analysis

## Team members

- Wu Wen Tang (ID 40028075)
- Zhen Yee (ID 40028478)
- Razvan Soos (ID 40035034)

## Abstract
This project is a dataset analysis of the [Yelp dataset](https://www.yelp.com/dataset), available to the public as JSON files. We will apply two techniques seen in the course using Apache Spark. The results will be discussed and interpreted.

The Yelp dataset is a subset of businesses, reviews and user data, written on the yelp review website, designed to be used for personal or educational purposes. There are multiple ways of using the Yelp dataset, including predicting restaurant [closure](https://towardsdatascience.com/using-yelp-data-to-predict-restaurant-closure-8aafa4f72ad6), popularity, etc. based on various factors such as restaurant density, review count, rating, and price relative to surrounding restaurants. Additionally, the yelp dataset provides user information, reviews or tips users left to businesses which can be used to study a pattern between users and pictures of the food, drinks, menu or restaurant which can be used for image classification. 

In this report, we analyze the results of a recommender system built based on the yelp dataset in order to recommend restaurants to users similar to the ones they’ve rated highly. This report aims to discuss the methods we used to process the original yelp data and the performance of our system.


## I. Introduction
### I.a. Context
A recommender system is an algorithm that provides relevant information to a given user by finding patterns or similarities in a dataset. The algorithm would rate the items and shows the user the items that they would rate highly. Some of the most famous examples of recommender systems are: Amazon, items are recommended to you that the algorithm deemed to be relevant, Spotify, which recommends relevant music to the user, or Netflix, which recommends certain movies based on user accounts. In class, we learned about content based and collaborative filtering recommender systems. This project will focus on collaborative filtering recommender systems, where the preference of a group of users is used to make recommendations to other users. An example of this would be recommending a restaurant to a user because their friend liked the restaurant. Therefore, user-user collaborative filtering is relevant to our project. The goal is to find a set of users whose ratings are similar to the given user's ratings, in order to be able to recommend restaurants to the given user. In other words, a restaurant will be recommended to a given user based on the fact that the same restaurant have been liked by other similar users.

### I.b. Objectives

The objective of this research is to build a recommender system based on user ratings of restaurants. In our research, when two users 1 and 2 go to the same restaurants A and B, the similarity index of these two users is computed. Then, depending on the score, the system can recommend restaurant C to user 2 because these two users are similar in terms of the restaurants they visit. 

### I.c. Related work

In regards to the related work, there are many other projects using the Yelp dataset, papers written using the Yelp dataset, as well as other projects made on the analysis of the dataset. Some examples are discussed below:

[Yelp recommendation](https://github.com/chanship/yelpRecommendation): Data mining is done with the Yelp dataset. They found the frequent itemsets in subsets of the Yelp dataset. They used Jaccard Similarity to identify similar user and business set. Then, they predicted the ratings/stars for the given user ids and business ids, an example of applying user-based collaborative filtering. 

This project looks very similar to ours, they apply many of the algorithms that we learned in class, as well as a few that we have not heard about. 

[SON implementation](https://github.com/manjar-cs/SON_Implementation): The SON algorithm (performs the Apriori algorithm) is implemented using the Apache Spark Framework. The goal of this project is to find frequent itemsets in two datasets: one simulated dataset(small1.csv,small2.csv), and one real-world dataset (generated from Yelp dataset). They want to apply the algorithm on large datasets more efficiently in a distributed environment.

This project is less relevant to our project, but still interesting because you can check how they convert the Yelp data. We will be converting the Yelp data from JSON to csv using pandas.

## II. Materials & Methods
### II.a. Dataset
The dataset used is the Yelp Open dataset. There are APIs available to extract the data from this dataset. This [website](https://www.kaggle.com/yelp-dataset/yelp-dataset/version/6#yelp_business_attributes.csv) gives a lot of information on the Yelp dataset. It's a great resource to view the information available.

The _Yelp dataset_ contains many attributes such as hours, parking, availability, ambience, etc. It also contains full review text data including user_id that wrote the review, the business_id the review is written for, date, etc. It is around 10GB. The information that is interesting to us in the scope of this project is in the following JSON files:
- yelp_academic_dataset_business.json
- yelp_academic_dataset_review.json

The other files will be disregarded. 

Preparing the data
The dataset is cleaned up first, filtering for restaurants only in the city of Toronto. There are nail salons and other businesses that were included, so everything that is not categorized as restaurants, food, fast food or bars were removed. Out of those restaurants, we filtered by restaurants that are open. Then, the JSON file was transformed and removed all the unnecessary columns, and linked it to the review file that was also edited. This results in a CSV file with the following column of every business that has all its reviews listed:

- business_id
- city
- name
- stars
- review stars
- user_id

Some lines were taken out because of the name syntax or special characters. To further reduce the dataset, only restaurants with a minimum review count of 50 were kept, there are now 290,900 lines. There are 1925 restaurants in the cleaned up dataset, which averages to around 150 reviews per restaurant. The code relating to this can be found in `cleaner.py`.


### II.b. Technologies
The technologies that will be used is Apache Spark.

_Apache Spark_

Apache Spark is built around RDDs, a dataset distributed over a cluster of machines. It was developed to overcome the limitations of MapReduce cluster computing model; and extends the model. Spark is more efficient in both iterative algorithms, and exploratory data analysis (e.g. the repeated database-style querying of data). Spark has in-memory cluster computing, which increases the processing speed of an application. Spark automatically distributes the data in RDDs across clusters and parallelizes the data.


### II.c. Algorithms
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

The code for our ALS implementation can be found in `/ALS_spark.py`

## III. Results

### III.a. Dataset analysis 
A matrix with users and businesses is a sparse matrix, because most users don't have many restaurant reviews. As seen by the graph below, most users have only 1 review.


It's difficult to give recommendations to users that didn’t review many restaurants, because there is no data about what they like so we won’t make recommendations for those users. This is also true especially if the restaurants don’t have many reviews either.

### III.b. Technology comparison or implementation
_Frequent itemsets_

The value for minimum support, where an itemset is identified as “frequent”, was picked to be 0.001, which means the restaurant appears once every 1000 reviews. It’s a very low value, but as mentioned above, there are many restaurants and not a lot of reviews from each user. Confidence indicates how often an association rule is found to be true. We set the minimum confidence for generating Association Rule to 0.001. Which means that if in the itemset restaurant A appears 1000 times, restaurant A and B co-occur 1 time. Again, this value is small because the number of reviews per user is low, so we had to decrease the value to obtain any results.

_ALS_

## IV. Discussion
### IV.a. Frequent itemsets
In Figure 2, we can see that the confidence level is quite low with a max confidence level of 0.211206689655172414. We think this is because over half the users reviewed only one restaurant, making the dataset of reviewed restaurants quite scattered for those users, meaning that each of those users reviewed different restaurants. 
As we can see from Figure 3, a lot of users are being recommended to similar restaurants by the recommender system, more noticeably the restaurant with business_id RtUvSWO_UZ8V3Wpj0n077w. We believe, again, this is due to over half the users only having reviewed a single restaurant. This means that over half the users are depending on the second half to have reviewed more restaurants than the first half. This makes it difficult for our recommender system to recommend a restaurant to users.
 
### IV.b. Alternating Least Square (ALS)

### IV.c. Limitations
The limitations of this project is related to the dataset and the data that can be obtained by it. Most people who go to restaurants do not end up rating it, unless they had an  extremely unsatisfying experience. Therefore, the data is very sparse and difficult to recommend restaurants to different types of users. However, since Yelp has a search feature, maybe some implicit data collection can be done based on the user’s search history and saved restaurant collections, and develop a recommender system based on a hybrid of the data instead of purely on restaurant ratings.


### IV.d. Future Work
For possible future work, it might be worth looking into using business categories instead of only sorting by restaurant names. Having categories opens up the possibility of sorting businesses by, for example, top or bottom categories based on the popularity of a restaurant. So if two users like the same low popularity restaurants, it could be factored in when recommending restaurants. This would probably result in better recommendations for more users. Another area for improvement would be to address the cold-start problem. In case of new users, the recommender could use the popularity based strategy and recommend popular restaurants, maybe based on local or regional or trends, and the time of the day. 



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
