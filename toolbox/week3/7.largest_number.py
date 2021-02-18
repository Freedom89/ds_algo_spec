# Uses python3

import sys


def is_greater_or_equal(x, y):
    # if the integer is negative - at the first step of loop
    # always return True
    if int(y) < 0:
        return True
    first_combi = int(f"{x}{y}")
    second_combi = int(f"{y}{x}")
    if first_combi >= second_combi:
        return True
    else:
        return False


# is_greater_or_equal(858,85)
# is_greater_or_equal(232, 23)
# is_greater_or_equal(202, 20)
# is_greater_or_equal(2, 21)


def largest_number(digits):
    # write your code here
    solution = []
    while len(digits) > 0:
        maxdigit = -999999
        for digit in digits:
            if is_greater_or_equal(digit, maxdigit):
                # if digit >= maxdigit:
                maxdigit = digit
        solution.append(maxdigit)
        digits.remove(maxdigit)
    formatted_solution = "".join(str(x) for x in solution)
    return formatted_solution


# digits = [858, 85, 20]
# largest_number([20, 99, 858, 85, 20])

if __name__ == "__main__":
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
