# Uses python3
import sys

#https://www.coursera.org/learn/algorithmic-toolbox/discussions/weeks/4/threads/IP3NQ-lEEeWFuw7QEATDpw

"""
get_majority(A[1...n]):

  if n == 1:
    return A[1] 
  {If there is only one element, it is the majority element}

  mid = n/2

  a = get_majority(A[1..mid])
  b = get_majority(A[mid+1...n])

  if a is not -1:
    count occurence of a in A
    if count > n/2:
      return a
  {this means a is the majority element for whole array}

  {Now repeat the procedure with majority element b}
  if b is not -1:
    count occurence of b in A
    if count > n/2:
      return b
  {this means b is the majority element for whole array}

  return -1 {if there is no majority element}
"""

def get_majority_element(seq, left, right):
    if left+1 == right:
        # only one element left, thus it must be the greatest
        return seq[left]
    # print(seq)
    midpoint = (left+right)//2
    greatest_left = get_majority_element(seq,left, midpoint)
    greatest_right = get_majority_element(seq,midpoint,right)

    majority_cutoff = (right-left)//2 #this will be the number of elements
    count_left, count_right = 0,0
    for number in seq[left:right]:
        if number == greatest_left:
            count_left+=1
        if number == greatest_right:
            count_right +=1
    if count_left>majority_cutoff and greatest_left != -1:
        return greatest_left
    elif count_right > majority_cutoff and greatest_right != -1:
        return greatest_right
    else:
        return -1

n = int(input())
seq_input = [int(i) for i in input().split()]

# seq_input = [1,2,3,4,5,6,7,8,8,8,8,8,8,8,8]
# n = len(seq_input)
# get_majority_element(seq_input, 0, n)

print(int(get_majority_element(seq_input, 0, n) != -1))

