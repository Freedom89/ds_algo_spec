# Uses python3


import numpy


def LCS3(s1, s2, s3, n1, n2, n3):
    """Finds the length of the longest common subsequence of three strings
    (str, str, str, int, int, int) -> (int, 3D-array)"""

    # Initializing the matrix
    Matrix = numpy.zeros((n1 + 1, n2 + 1, n3 + 1))

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            for k in range(1, n3 + 1):
                if s1[i - 1] == s2[j - 1] == s3[k - 1]:
                    Matrix[i][j][k] = Matrix[i - 1][j - 1][k - 1] + 1
                else:
                    Matrix[i][j][k] = max(
                        Matrix[i - 1][j][k], Matrix[i][j - 1][k], Matrix[i][j][k - 1]
                    )

    return (int(Matrix[-1][-1][-1]), Matrix)


n1, s1, n2, s2, n3, s3 = (
    int(input()),
    input(),
    int(input()),
    input(),
    int(input()),
    input(),
)
s1, s2, s3 = (
    [int(i) for i in s1.split()],
    [int(i) for i in s2.split()],
    [int(i) for i in s3.split()],
)

# s1 = [1, 2, 3]
# s2 = [2, 1, 3]
# s3 = [1, 3, 5]
# n1, n2, n3 = 3, 3, 3
LCS_length, Matrix = LCS3(s1, s2, s3, n1, n2, n3)
print(LCS_length)