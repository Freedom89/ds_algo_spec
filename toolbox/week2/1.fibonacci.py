# Uses python3
def calc_fib(n):
    if n <= 1:
        return n
    n_2 = 0
    n_1 = 1
    for i in range(n - 1):
        n = n_1 + n_2
        n_1, n_2 = n, n_1
    return n


n = int(input())
print(calc_fib(n))
