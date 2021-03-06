# Uses python3

import sys
import numpy


def LCS2(s1, s2, n1, n2):
    """Finds the length of the longest common subsequence of two strings
    (str, str, int, int) -> (int, 2D-array)"""

    # Initializing the matrix
    Matrix = numpy.zeros((n1 + 1, n2 + 1))

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                Matrix[i][j] = Matrix[i - 1][j - 1] + 1
            if s1[i - 1] != s2[j - 1]:
                Matrix[i][j] = max(Matrix[i][j - 1], Matrix[i - 1][j])

    return (int(Matrix[n1][n2]), Matrix)


"""
		2	3	1	2	4	5	6	7
1	0	0	0	1	1	1	1	1	1
2	0	1	1	1	2	2	2	2	2
3	0	1	2	2	2	2	2	2	2
4	0	1	2	2	2	3	3	3	3
5	0	1	2	2	2	3	4	4	4
6	0	1	2	2	2	3	4	5	5
7	0	1	2	2	2	3	4	5	6
"""
n1 = int(input())
s1 = [int(x) for x in input().split(" ")]
n2 = int(input())
s2 = [int(x) for x in input().split(" ")]

# s1 = [1, 2, 3, 4, 5, 6, 7]
# n1 = len(s1)
# s2 = [2, 3, 1, 2, 4, 5, 6, 7]
# n2 = len(s2)
print(LCS2(s1, s2, n1, n2)[0])
