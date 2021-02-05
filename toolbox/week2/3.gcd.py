# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    greater_num, smaller_num = max(a, b), min(a, b)
    while current_gcd:
        current_gcd = greater_num % smaller_num
        if current_gcd == 0:
            """
            This means the smaller num is currently the GCD
            """
            return smaller_num
        if current_gcd == 1:
            """
            This means there is no common GCD
            """
            return 1
        greater_num, smaller_num = smaller_num, current_gcd

    return current_gcd


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
