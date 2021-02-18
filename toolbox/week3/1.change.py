# Uses python3
import sys


def get_change(m):
    # write your code here
    tens, remainders = m // 10, m % 10
    fives, remainders = remainders // 5, remainders % 5

    return tens + fives + remainders


if __name__ == "__main__":
    m = int(sys.stdin.read())
    print(get_change(m))
