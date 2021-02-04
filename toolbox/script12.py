# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers: list):
    n = len(numbers)
    index_1: int = 0
    for first in range(1, n):
        if numbers[first] > numbers[index_1]:
            index_1 = first
    if index_1 == 0:
        index_2: int = 1
    else:
        index_2 = 0
    for second in range(1, n):
        if numbers[second] != numbers[index_1] and numbers[second] > numbers[index_2]:
            index_2 = second
    print(index_1, index_2)  # for verbose logging
    return numbers[index_1] * numbers[index_2]


def max_pairwise_product_fast_correct(numbers: list):
    index_1 = 0
    n = len(numbers)
    for i in range(1, n):
        if numbers[i] > numbers[index_1]:
            index_1 = i
    # change the last array to the biggest number
    # because python index starts from 0
    numbers[index_1], numbers[n - 1] = numbers[n - 1], numbers[index_1]
    index_2 = 0
    for i in range(1, n - 1):
        if numbers[i] > numbers[index_2]:
            index_2 = i
    numbers[index_2], numbers[n - 2] = numbers[n - 2], numbers[index_2]
    # print(index_1, index_2)
    return numbers[n - 1] * numbers[n - 2]


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    # print(max_pairwise_product(input_numbers))
    # print(max_pairwise_product_fast(input_numbers))
    print(max_pairwise_product_fast_correct(input_numbers))
