# Uses python3
import sys


def get_fibonacci_huge(n, m=10):
    """
    This is from question 5
    """
    period = 60  # This is from question5, where calc_period(10) = 60
    new_n = n - period * (n // period)
    if new_n <= 1:
        return new_n
    next = 0
    next_next = 1
    for i in range(new_n - 1):
        next_next, next = (next_next + next) % m, next_next
    return next_next


def fibonacci_sum(n):
    """
    The trick is to add +2
    """
    total_value = get_fibonacci_huge(n + 2)
    if total_value == 0:
        total_value += 10
    return total_value - 1


def fibonacci_partial_sum(from_, to):
    total_m = fibonacci_sum(to)
    total_n = fibonacci_sum(from_ - 1)
    """
    If m is not sufficient to minus from n, then we need to add "10".
    e.g 3-7 is not sufficent, so 13-7 = remainder 6 
    """
    if total_m < total_n:
        total_m += 10
    return total_m - total_n


if __name__ == "__main__":
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))