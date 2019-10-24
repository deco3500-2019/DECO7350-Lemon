"""
The code is to use the binary algorithm Naive Bayes to perform the analysis for the relationships between user activities
and sleep quality

---------------------------------------------------------------------------------------------------------------------

For each column in the dataset, it represents the presence of particular activity, including caffeine related drinks, alcohol,
nap, sleep runine, and big meal. The last column represents sleep quality. We used 1 to represent the presence of activities,
and 0 represents the absence. Following is a example for the dataset:

caffeine related drinks     alcohol         nap         sleep runtine         big meal     sleep quality

        0                       1            0                1                   1              1
        1                       1            1                1                   0              1
        0                       1            0                0                   0              0
        
        
 
---------------------------------------------------------------------------------------------------------------------

The Naive Bayes Importance we used as:

Importance = log(p(c =1 | L= 1)) - log(p(c = 0 | L = 1))

---------------------------------------------------------------------------------------------------------------------

We used Lapcae Smoothing to avoid some activities are not presence in all records

We choosed 0.3 as threshold. The probability which over 0.3 indicates that this activity has positive influence in his/her
sleep quality. The probability which less than 0.3 indicates that this activity doesn't have direct relationship with user
sleep quality




