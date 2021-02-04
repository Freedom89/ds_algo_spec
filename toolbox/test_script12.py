# python3
import script12 as func  # type: ignore
from numpy.random import seed, randint


def stress_test(N: int, M: int):
    seed(1)
    condition = True
    while condition:
        n = randint(2, N)  # generate random number
        A = [0] * n  # array of size n
        for i in range(n):
            A[i] = randint(0, M)
        print(A)
        result1 = func.max_pairwise_product(A)
        result2 = func.max_pairwise_product_fast(A)
        if result1 == result2:
            print("OK")
        else:
            print("WRONG ANSWER")
            return A


wrong_answer = stress_test(10, 10)

"""
[7, 9, 8, 6, 9, 3, 7, 7, 4]
1 2
WRONG ANSWER
"""
temp_wrong_answer = [5, 1, 4, 6, 0, 6, 5, 1, 2]
# turns out what if there is repeated integers
