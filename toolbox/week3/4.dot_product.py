# Uses python3

import sys


def max_dot_product(a, b):
    # write your code here
    a = sorted(a, key=lambda x: -x)
    b = sorted(b, key=lambda x: -x)
    return sum([x * y for x, y in zip(a, b)])


# max_dot_product([1, 3, -5], [-2, 4, 1])

if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1 : (n + 1)]
    b = data[(n + 1) :]
    print(max_dot_product(a, b))
