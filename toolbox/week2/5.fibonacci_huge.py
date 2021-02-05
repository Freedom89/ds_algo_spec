# Uses python3
import sys


def calc_period(m):
    """
    Watch this video to understand how to calculate the Pisano period
    IT IS NOT 2^m
    You can watch at 7:30 seconds
    # https://www.youtube.com/watch?v=Nu-lW-Ifyec
    Ref table for the values
    http://webspace.ship.edu/msrenault/fibonacci/fiblist.htm
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


def get_fibonacci_huge_naive(n, m):
    """
    Also note this property of fiboancci
    f_n mod m = f_{n-1} mod m + f_{n-2} mod m
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


# get_fibonacci_huge_naive(239, 1000)

# get_fibonacci_huge_naive(2816213588, 239)

if __name__ == "__main__":
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
