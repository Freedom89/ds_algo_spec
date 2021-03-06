# Uses python3
import sys
import random

def partition3(array, left, right):
    # first part of the code
    # for all numbers less than or equals to
    # the first number in the divided array,
    # move it to the left 
    marker = left
    first_num = array[left]
    for index in range(left+1,right):
        if array[index] <= first_num:
            # if there is a number smaller than the first_num,
            # move it to the next spot from left 
            array[index],array[marker+1] = array[marker+1],array[index]
            marker +=1
    # Finally, switch the first number with where the marker is left off        
    array[left],array[marker] = array[marker],array[left]
    # print(array)
    # In the next iteration, for all values less than where the marker is
    # move it to the left. 

    marker_left = left
    for index in range(left,marker):
        if array[index] < array[marker]:
            # if the number in the spot is less than the partition number,
            # move it to the left where the second marker is
            array[index],array[marker_left] = array[marker_left],array[index]
            # print(array)
            # move the marker into another spot
            marker_left +=1

    return marker_left, marker



def quicksort3(array,left,right):
    #This means the array is only size 1, nothing to sort
    if left+1 >= right: 
        return 
    
    # take a random number from 0 to n-1 (since python starts from 0)
    random_marker = random.randint(left,right-1)
    # switch the random number to be the first element
    array[left], array[random_marker] = array[random_marker], array[left]

    marker_left, marker_right = partition3(array, left,right)
    quicksort3(array, left, marker_left)
    quicksort3(array,marker_right+1,right)

# seq = [4,4,36,7,2,4,1,5,1,3,6,25,1]
# partition3(seq,0,len(seq))
# quicksort3(seq,0,len(seq))

# seq = [2,3,9,2,9]
# quicksort3(seq,0,len(seq))

n = int(input())
seq = [int(i) for i in input().split()]
quicksort3(seq,0,len(seq))
for x in seq:
    print(x, end=' ')


# ORGINAL CODE
# def partition2(a, l, r):
#     x = a[l]
#     j = l
#     for i in range(l + 1, r + 1):
#         print(a)
#         if a[i] <= x:
#             j += 1
#             print('triggered',i,a[i],j,a[j])
#             a[i], a[j] = a[j], a[i]
#     print(a)        
#     print("finally")
#     a[l], a[j] = a[j], a[l]
#     print(a)
#     return j

# seq = [4,36,7,2,4,1,5,1,3,6,25,1]
# partition2(seq,0,len(seq)-1)

# def randomized_quick_sort(a, l, r):
#     if l >= r:
#         return
#     k = random.randint(l, r)
#     a[l], a[k] = a[k], a[l]
#     #use partition3
#     m = partition2(a, l, r)
#     print("split", m)
#     randomized_quick_sort(a, l, m - 1);
#     randomized_quick_sort(a, m + 1, r);


# a = [40,4,36,7,2,4,1,5,1,3,6,25,1]
# n = len(a)
# random.seed(1)
# randomized_quick_sort(a, 0, n - 1)
# for x in a:
#     print(x, end=' ')
