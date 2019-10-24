
""" This code is to perform analysis for the first column data, which represents the users who have
    take the Caffeine related beverage.

    The code deploys the Naive Bayes for analysing the different situation
    We implicitly regard each variable is independent, and the different column has no effects on others

    The importance for our Naive Bayes Method is :

    Importance = log(p(c =1 | L= 1)) - log(p(c = 0 | L = 1))
"""
import math
a = open("5.txt", "r")
for d_line in a:
    dt_line = d_line.strip().split(" ")
    b = open("caffeine.txt", "a+")
    b.write(str(dt_line[0]))
    b.write(" ")
    b.write(str(dt_line[5]) + '\n')
    b.close()
a.close()

positive = float()
negative = float()

c = open("caffeine.txt", "r")
for cf_line in c:
    cafei = cf_line.strip().split(" ")
    if float(cafei[0]) == 1:
        if float(cafei[0]) == 1:
            positive = positive + 1
        else:
            negative = negative + 1
c.close()

""" The Naive Bayes, within Lapcae Smoothing """
probability = math.log((positive + 1) / (positive + negative + 2)) - math.log((negative + 1) / (positive + negative + 2))


print(probability)


# if probability < 0.3:
#     print("Please drink coffeer")
# else:
#     print(" dont drinl coffee")





