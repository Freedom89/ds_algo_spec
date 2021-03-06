input = "17 59 34 57 17 23 67 1 18 2 59".split(" ")
input = [int(x) for x in input]
input
sum(input) // 3

# if it is possible to split into 3,
# this means the first number must be combine with some other number


# once we extract the first combination,
# split the remaining 2

first_array = []
second_array = []
third_array = []

import numpy as np

# my first job is to extract 118 from the portfolio
matrix = np.zeros()
for element in input:

# [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]

def partitions(W, n, items):
    """ Finds if number of partitions having capacity W is >=3
    (int, int, list) -> (int) """
    count = 0 
    value = np.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if items[j-1]<=i:
                temp = value[i-items[j-1]][j-1] + items[j-1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == W: count += 1
    
    if count < 3: print('0')
    else: print('1')
    return value

a = partitions(118, len(input),input)    