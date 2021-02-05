# Uses python3
from sys import stdin

"""
the trick is basically shown in the rectangle. 
1. To calculate 273 = 13 * 21 
2. This means to calculate F_0^2 to F_n^2, it is f_n * f_(n+1)
3. To get the last digit, simply take the last digit, multiply, and take last digit
4. We make use of question 6 to compute large fibonacci numbers
"""


def calc_period(m):
    """
    from question6
    """
    counter = 0
    next = 0
    next_next = 1
    condition = True
    while condition:
        next, next_next = next_next, (next_next + next) % m
        counter += 1
        if next == 0 and next_next == 1:
            condition = False

    return counter


def get_fibonacci_huge(n, m):
    """
    from question 6
    """
    period = calc_period(m)  # calculating the period
    new_n = n - period * (n // period)  # remainder of n divide by the piasano period
    if new_n <= 1:
        return new_n
    next = 0
    next_next = 1
    for i in range(new_n - 1):
        next_next, next = (next_next + next) % m, next_next
    return next_next


def fibonacci_sum_squares(n):
    length = get_fibonacci_huge(n + 1, 10)  # last digit of the length
    breath = get_fibonacci_huge(n, 10)  # last digit of the breath
    squared_last_digit = (length * breath) % 10
    return squared_last_digit


if __name__ == "__main__":
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
