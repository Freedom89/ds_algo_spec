# Uses python3
import sys


def possible_prev_steps(x):
    possible_steps = []
    if x // 3 == x / 3:
        possible_steps.append(x // 3)
    if x // 2 == x / 2:
        possible_steps.append(x // 2)
    possible_steps.append(x - 1)
    return possible_steps


def get_min_steps(_possible_steps, _dict_of_steps):
    steps_tracker = []
    for i in _possible_steps:
        steps_tracker.append(_dict_of_steps.get(i)[0])
    min_index = steps_tracker.index(min(steps_tracker))
    return min(steps_tracker) + 1, _possible_steps[min_index]


def solution(x):
    steps = {1: (0, 1), 2: (1, 1), 3: (1, 1)}
    if x == 1:
        return 0, [1]
    if x <= 3:
        return 1, [1, x]
    # dict format: number_index, (operations, previous number)
    for i in range(4, x + 1):
        possible_steps = possible_prev_steps(i)
        best_previous_step = get_min_steps(possible_steps, steps)
        steps.update({i: (best_previous_step[0], best_previous_step[1])})

    backtrace, value = [x], x
    while len(backtrace) <= best_previous_step[0]:
        value = steps[value][1]
        backtrace.insert(0, value)
    return best_previous_step[0], backtrace


n = int(input())
n_out, list_out = solution(n)
print(n_out)
print(*list_out, sep=" ")


# from itertools import product


# def solution2(n):
#     found = False
#     answer = n - 1
#     for k in range(1, n):
#         # enumerate all sequences of operations (+1, *2, *3)
#         for seq in product([0, 1, 2], repeat=k):
#             start = 1
#             for i in seq:
#                 if i == 0:
#                     start += 1
#                 if i == 1:
#                     start *= 2
#                 if i == 2:
#                     start *= 3
#             # if a sequence leads to n update the answer
#             if (not found) and (start == n):
#                 found = True
#                 answer = k
#         if found:
#             break
#     return answer


# for i in range(1, 10 ** 6):
#     sol1 = solution(i)[0]
#     sol2 = solution2(i)
#     if sol1 != sol2:
#         print(i)
#         break
