# 499-dataset-analysis

## Team members

- Wu Wen Tang (ID 40028075)
- Zhen Yee (ID 40028478)
- Razvan Soos (ID 40030524)

## Abstract
This project is a dataset analysis of the [Yelp dataset](https://www.yelp.com/dataset), available to the public as JSON files. We will apply two techniques seen in the course using Apache Spark. The results will be discussed and interpreted.

The Yelp dataset is a subset of businesses, reviews and user data, written on the yelp review website, designed to be used for personal or educational purposes. There are multiple ways of using the Yelp dataset, including predicting restaurant [closure](https://towardsdatascience.com/using-yelp-data-to-predict-restaurant-closure-8aafa4f72ad6), popularity, etc. based on various factors such as restaurant density, review count, rating, and price relative to surrounding restaurants. Additionally, the yelp dataset provides user information, reviews or tips users left to businesses which can be used to study a pattern between users and pictures of the food, drinks, menu or restaurant which can be used for image classification. 

In this report, we analyze the results of a recommender system built based on the yelp dataset in order to recommend restaurants to users similar to the ones they’ve rated highly. This report aims to discuss the methods we used to process the original yelp data and the performance of our system.


## I. Introduction
### I.a. Context
A recommender system is an algorithm that provides relevant information to a given user by finding patterns or similarities in a dataset. The algorithm would rate the items and shows the user the items that they would rate highly. Some of the most famous examples of recommender systems are: Amazon, items are recommended to you that the algorithm deemed to be relevant, Spotify, which recommends relevant music to the user, or Netflix, which recommends certain movies based on user accounts. This project will focus on collaborative filtering recommender systems, where the historical preference of a group of users is used to make recommendations to other users. The ratings that will be taken in consideration are explicit ratings, meaning they’re based on a numerical value users gave to restaurants as a rating. Additionally, this project will also consider frequent itemsets, looking to recommend a restaurant highly rated by a first user to a second user who has similar tastes in restaurants as the first user.

### I.b. Objectives

The objective of this research is to build a recommender system based on user ratings of restaurants that will accurately predict and recommend restaurants to its users. In other words, the goal of this project is to, given numerical user ratings, accurately recommend a set of restaurants liked by certain users to another group that only liked a part of the set.

### I.c. Related work

In regards to the related work, there are many other projects using the Yelp dataset, papers written using the Yelp dataset, as well as other projects made on the analysis of the dataset. Some examples are discussed below:

[Yelp recommendation](https://github.com/chanship/yelpRecommendation): Data mining is done with the Yelp dataset. They found the frequent itemsets in subsets of the Yelp dataset. They used Jaccard Similarity to identify similar user and business set. Then, they predicted the ratings/stars for the given user ids and business ids, an example of applying user-based collaborative filtering. 

This project looks very similar to ours, they apply many of the algorithms that we learned in class, as well as a few that we have not heard about. 

[SON implementation](https://github.com/manjar-cs/SON_Implementation): The SON algorithm (performs the Apriori algorithm) is implemented using the Apache Spark Framework. The goal of this project is to find frequent itemsets in two datasets: one simulated dataset(small1.csv,small2.csv), and one real-world dataset (generated from Yelp dataset). They want to apply the algorithm on large datasets more efficiently in a distributed environment.

This project is less relevant to our project, but still interesting because you can check how they convert the Yelp data. We will be converting the Yelp data from JSON to csv using pandas.

## II. Materials & Methods
### II.a. Dataset
The dataset used is the Yelp Open dataset. It contains many attributes such as hours, parking, availability, ambience, etc. It also contains full review text data including user_id that wrote the review, the business_id the review is written for, date, etc. It is around 10GB. The information that is interesting to us in the scope of this project is in the following JSON files:
- yelp_academic_dataset_business.json
- yelp_academic_dataset_review.json

The other files will be disregarded. 

Preparing the data
The dataset is cleaned up first, filtering for only for open restaurants. There are nail salons and other businesses that were included, so everything that is not categorized as restaurants, food, fast food or bars were initially removed. Later on we also decided to remove fast food and bars since our dataset was more than big enough. We finally filtered the business file to only contain restaurants within Toronto and then dropped the columns that wouldn't serve any purpose. Next, we used chunks to parse the review file since it contains millions of reviews and it's easier on our system to use chunks. The datatypes were also identified to speed things up. As we were going through the file, we dropped everything besides the busines_id, user_id and the stars that we renamed to review star, not to create confusion with the actual stars of the restaurant. Finally everything was concated together to join each business with its reviews and create a file having the following header:
- business_id
- city
- name
- stars
- review stars
- user_id

Some lines were taken out because of the name syntax or special characters. To further reduce the dataset, only restaurants with a minimum review count of 50 were kept, there are now 290,900 lines. There are 1925 restaurants in the cleaned up dataset and 80343 users, which averages to around 150 reviews per restaurant. The code relating to this can be found in `cleaner.py` and `counter.py`


### II.b. Technologies
The technologies that will be used are Apache Spark, Pandas and Matplotlib.

_Apache Spark_

Apache Spark is built around RDDs, a dataset distributed over a cluster of machines. It was developed to overcome the limitations of MapReduce cluster computing model; and extends the model. Spark is more efficient in both iterative algorithms, and exploratory data analysis (e.g. the repeated database-style querying of data). Spark has in-memory cluster computing, which increases the processing speed of an application. Spark automatically distributes the data in RDDs across clusters and parallelizes the data. The core of our algorithms reside on spark.

_Pandas_

Pandas is a python library designed for data analysis. It provides high-performance, easy to use structures and data analysis tools. In our project, it was used to extract the relevant data out of the dataset and to rearrange the data in order to be able to perform algorithms on it and to understand it once those algorithms are performed.

_Matplotlib_

Matplotlib is a plotting library for Python and NumPy. It is designed to function a bit like matlab and to plot figures given code. In our project, it was used to showcase what our final dataset looked like and to help us understand what we're working with. The code to plot our graphs can be found in `graphs.py` and the graphsthat were produced can be found in the folder [graphs](https://github.com/wuwentang/499-dataset-analysis/tree/master/graphs)

### II.c. Algorithms
_Frequent Itemsets_

The goal of frequent itemsets is to find sets of items that appear frequently together in "baskets". Frequent itemsets are generated by a set of items that appear in a defined number of support threshold s. Frequent itemset mining leads to associations between items in large data sets. Once the frequent itemsets are generated, association rules can be formed in the format of {item A} => {item B}.

In our case, frequent itemsets will be used to find frequent itemsets of restaurants per user. This can be used to find users who have similar tastes in restaurants, in user-based collaborative filtering. For example, 

Items = {Boustan, Wienstein & Gavino's, Pho Lien, Amir, M4 Burritos}

Support threshold = 3

B1 = {B, W, P}, B2 = {B, A, M}, B3 = {A, M}, B4 = {B, P}, B5 = {B, P, A, M}, ...

Frequent itemsets: {B}, {P}, {M}, {B, P}, {A, M}

For our project, we filtered the data with `business_id`, `user_id`, `avg_star`, and `reviewer_star` which will allow us to further filter the data where a user reviews a restaurant that is higher than or equal to the average star of the restaurant.

This was an assumption we made to filter out bad reviews, because we want our recommender system to recommend restaurants to users who had a positive experience at the restaurant. 

The code for our Frequent Itemsets implementation can be found in `/fp_growth.py`.

_Alternating least Square (ALS)_

Matrix factorization algorithm is used to solve issues with collaborative filtering recommenders such as popularity bias,  cold-start problem, and scalability issue when more data is added to the data set. In a user-item interaction matrix, the data is also often sparse. For collaborative filtering, matrix factorization algorithms decompose the user-item interaction matrix into two matrices that are lower in dimension: one for the users, and one for the items.

ALS is a matrix factorization algorithm and and is implemented in Spark. It is used for collaborative filtering with large data sets. In this project, it is applied because it scales well to large datasets and can solve the sparseness problem of the restaurants ratings data. [Here](https://towardsdatascience.com/prototyping-a-recommender-system-step-by-step-part-2-alternating-least-square-als-matrix-4a76c58714a1) is an example for implementing a minimum viable product (MVP) ALS recommender system.

The code for our ALS implementation can be found in `/ALS_spark.py`

## III. Results

### III.a. Dataset analysis 
A matrix with users and businesses is a sparse matrix, because most users don't have many restaurant reviews. As seen by the graph below, most users have only 1 review.

<p align="center">Figure 1. Review per person

<p align="center"><img src="/graphs/review_per_person_max20.png" height="400" />

Since we have 80343 users and 1925 restaurants, the matrix of users restaurants has 154660275 squares, of which only 290900 are filled, which makes 99.81% of the matrix empty. It's difficult to give recommendations to users that didn’t review many restaurants, because there is no data about what they like. This is also true especially if the restaurants don’t have many reviews either. We attempted giving suggestions to users with 1 or 2 reviews but the confidence of the algorithm is very low for them, therefore for the frequent itemsets algorithm, we decided to remove users with too little reviews.

### III.b. Technology comparison or implementation
_Frequent itemsets_

The value for minimum support, where an itemset is identified as “frequent”, was picked to be 0.001, which means the restaurant appears once every 1000 reviews. It’s a very low value, but as mentioned above, there are many restaurants and not a lot of reviews from each user. Confidence indicates how often an association rule is found to be true. We set the minimum confidence for generating Association Rule to 0.001. Which means that if in the itemset restaurant A appears 1000 times, restaurant A and B co-occur 1 time. Again, this value is small because the number of reviews per user is low, so we had to decrease the value to obtain any results.

_ALS_

The values for the ALS function were chosen by trial and error, trying to optimize and find the lowest rmse possible. It was found that with a maxIter of 5 and a rank of 25, the best results are produced when redParam is 0.4, resulting in an rmse of 1.20. Considering how empty our matrix  is, as discussed previously, we judged that a 1.20 rmse is acceptable. Our system can take as parameter a numerical value as a max number of recommendations per user and returns the desired amount of recommendations for every user with their respective rating. Some ratings were found to be very low, whereas others were more acceptable. An example will be shown in discussion.

## IV. Discussion
### IV.a. Frequent itemsets
In Figure 3, we can see that the confidence level is quite low with a max confidence level of `0.211206689655172414`. We think this is because over half the users reviewed only one restaurant, making the dataset of reviewed restaurants quite scattered for those users, meaning that each of those users reviewed different restaurants. 

As we can see from Figure 4, a lot of users are being recommended to similar restaurants by the recommender system, more noticeably the restaurant with `business_id` `RtUvSWO_UZ8V3Wpj0n077w`. We believe, again, this is due to over half the users only having reviewed a single restaurant. This means that over half the users are depending on the second half to have reviewed more restaurants than the first half. This makes it difficult for our recommender system to recommend a restaurant to users.

<p align="center"><img src="graphs/result_of_frequent_itemset.png" height="400" />
 
<p align="center">Figure 2. Result of Frequent Itemset

<p align="center"><img src="/graphs/result_association_rule.png" height="400" />

<p align="center">Figure 3. Result of Association Rule

<p align="center"><img src="graphs/result_of_transformation.png" height="400" />
 
<p align="center">Figure 4. Result of Transformation and Predictions (a more detailed prediction can be found in /FP-Growth-Predictions)
 
### IV.b. Alternating Least Square (ALS)
In figure 5, we can see that certain users have strong first ratings, such as 9.285 or 11.425 whereas others have much lower ratings for the recommendations such as 1.402 or 2.539. The reasoning behind this discrepancy in results is that the system has a hard time recommending a restaurant with certainty to a user that has only 1 review. We’ve set the maximum number or restaurants recommended to 10 because besides a few exceptions such as food critics who have hundreds of reviews, the rating becomes too low for the recommendation to have any significance. An argument could have been made to lower the maximum recommendations to 5 or even 3 for users who already have a low rating on their first recommendation such as the 1.402 user mentioned previously. Alternatively, for better results and more relevance, users with less than 10 reviews could have been removed from the dataset to have much more precise recommendations and higher average rating across the board.

<p align="center"><img src="/graphs/als_recommender.png" height="400" />
<p align="center">Figure 5. Results of the ALS recommender for the first 10 users alphabetically

### IV.c. Limitations
The limitations of this project is related to the dataset and the data that can be obtained by it. Most people who go to restaurants do not end up rating it, unless they had an  extremely unsatisfying experience. Therefore, the data is very sparse and difficult to recommend restaurants to different types of users. However, since Yelp has a search feature, maybe some implicit data collection can be done based on the user’s search history and saved restaurant collections, and develop a recommender system based on a hybrid of the data instead of purely on restaurant ratings.


### IV.d. Future Work
For possible future work, it might be worth looking into using business categories instead of only sorting by restaurant names. Having categories opens up the possibility of sorting businesses by, for example, top or bottom categories based on the popularity of a restaurant. So if two users like the same low popularity restaurants, it could be factored in when recommending restaurants. This would probably result in better recommendations for more users. Another area for improvement would be to address the cold-start problem. In case of new users, the recommender could use the popularity based strategy and recommend popular restaurants, maybe based on local or regional or trends, and the time of the day. 



## References

https://en.wikipedia.org/wiki/Apache_Spark

https://towardsdatascience.com/how-to-build-a-simple-recommender-system-in-python-375093c3fb7d

https://towardsdatascience.com/prototyping-a-recommender-system-step-by-step-part-2-alternating-least-square-als-matrix-4a76c58714a1

https://www.sciencedirect.com/topics/computer-science/frequent-itemsets

https://www.edureka.co/blog/apriori-algorithm/#association-rules

https://github.com/chanship/yelpRecommendation

https://github.com/manjar-cs/SON_Implementation
