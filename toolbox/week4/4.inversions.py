# Uses python3
import sys
# https://www.youtube.com/watch?v=Vj5IOD7A6f8
# the exact algorthim is at 27:03
total_count = 0

def merge(left_array,right_array):
    i, j, inversion_counter = 0,0,0
    final = []
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            final.append(left_array[i])
            i += 1
        else:
            final.append(right_array[j])
            # This formula is from the youtube video
            # Correctness please follow up
            inversion_counter += len(left_array) - i
            j +=1

    final += left_array[i:]
    final += right_array[j:]

    return final, inversion_counter


def merge_sort(array):
    global total_count
    if len(array)==1:
        return array #nothing to sort 
    midpoint = len(array) // 2
    left_arr = merge_sort(array[:midpoint])
    right_arr = merge_sort(array[midpoint:])

    sorted_arr,temp = merge(left_arr,right_arr)
    total_count += temp

    return sorted_arr

n = int(input())
seq = [int(i) for i in input().split()]
merge_sort(seq)
print(total_count)