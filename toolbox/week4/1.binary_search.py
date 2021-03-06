# Uses python3
import sys

def binary_search(a, x):
    # left, right = 0, len(a)
    # write your code here
    input_list = a
    search_number = x
    # input_list = [1,5,8,12,13]
    # search_number = 11
    found = False
    left, right = 0, len(input_list) -1
    while not found:
        search_index = (left+right)//2 
        # print(search_index, left ,right)
        if( input_list[search_index] == search_number):
            # if the search index is the number, end the while loop
            found = True
        elif (left >= right):
            # if the search space only left with only 0 or 1
            # element left in the list, means the number cannot be found
            # we then break the list
            break
            # print("None")
        elif(input_list[search_index] > search_number):
            # since it is a sorted list,
            # if the number is greater than the search,
            # we move to the left side of the list
            right = search_index -1
        else:
            # else, we move to the right of the list
            left = search_index +1
    if found:
        return search_index
    else:
        return -1



def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [5,1,5,8,12,13,5,8,1,23,1,11]
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        # print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end = ' ')
