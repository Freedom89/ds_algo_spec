# python3

import sys
import threading


# nodes = [4, -1, 4, 1, 1]
# nodes = [-1, 0, 4, 0, 3]


def compute_height(n, nodes):
    tree_list = [[] for x in range(n)]
    root = None
    for node, parent in enumerate(nodes):
        # print(node, parent)
        if parent == -1:
            root = node
        else:
            tree_list[parent].append(node)

    height = 1
    found = False
    next_level = [root]
    next_next_level = []
    while not found:
        for current_node in next_level:
            next_next_level += tree_list[current_node]
        if len(next_next_level) == 0:
            break
        next_level = next_next_level
        next_next_level = []
        height += 1
    return height


# def compute_height(n, parents):
#     # Replace this code with a faster implementation
#     max_height = 0
#     for vertex in range(n):
#         height = 0
#         current = vertex
#         while current != -1:
#             height += 1
#             current = parents[current]
#         max_height = max(max_height, height)
#     return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()
