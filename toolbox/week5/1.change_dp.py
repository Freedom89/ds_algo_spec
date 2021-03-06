# Uses python3
import sys


def get_change(m):
    # coin types - 1,3,4
    init_tuple = [1, 2, 1, 1]
    # 1 way to generate 1 coin, 2 ways for 2, 1 way for 3
    if m <= 4:
        return init_tuple[m - 1]
    else:
        for _ in range(5, m + 1):
            # the n-coin is always the previous 4 steps add 1
            init_tuple.append(min(init_tuple[-4:]) + 1)
    return init_tuple[-1]


n = int(input())
print(get_change(n))