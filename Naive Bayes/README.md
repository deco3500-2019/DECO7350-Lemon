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
