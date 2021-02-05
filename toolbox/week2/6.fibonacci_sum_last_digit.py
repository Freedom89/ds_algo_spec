# Uses python3
# %%
import sys

# %% [markdown]
# The special trick is to know that

# $$
# \sum_i^n F_i = F_{n+2} - 1 \\
# $$

# $$
# \begin{aligned}
# F(n+2) &= F(n+1) + F(n) \\
#  &= F(n) + F(n-1) + F(n) \\
# &= F(n) + F(n-1) + F(n-1) + F(n-2) \\
# &= F(n) + F(n-1) + F(n-2) + F(n-2) + F(n-3) \\
# &= F(n) + ... + F(1) + F(1) + F(0)
# \end{aligned}
# $$
# %%


def get_fibonacci_huge(n, m=10):
    """
    Also note this property of fiboancci
    f_n mod m = f_{n-1} mod m + f_{n-2} mod m
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


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
