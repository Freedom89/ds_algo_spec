# Uses python3
import sys


def optimal_summands(n):
    summands = []
    i = 1  # i has to start from 1
    while i <= n:
        summands.append(i)
        # remove from the prize pool for each i rewarded
        n -= i
        # increase to the next prize
        i += 1
        # if the next is more than the remainder, just allocate
        # the remainder to the best winnder
        if i > n:
            summands[-1] += n
    return summands


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=" ")
