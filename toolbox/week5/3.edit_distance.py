def levenshteinDistance(s1, s2):
    # s2 is always the longer distance
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2 + 1]
        for i1, c1 in enumerate(s1):

            if c1 == c2:
                distances_.append(distances[i1])
                # print(c1, c2, distances[i1])
            else:
                distances_.append(
                    1 + min((distances[i1], distances[i1 + 1], distances_[-1]))
                )
                # print(
                #     c1, c2, 1 + min((distances[i1], distances[i1 + 1], distances_[-1]))
                # )
        distances = distances_
        # print(distances)
    return distances[-1]


# levenshteinDistance("editing", "distance")

"""
This is how the algo works
		d	i	s	t	a	n	c	e
	0	1	2	3	4	5	6	7	8
e	1	1							
d	2	1							
i	3	2							
t	4	3							
i	5	4							
n	6	5							
g	7	6							
			
[1, 1, 1, 2, 3, 4, 5, 6]
[2, 2, 2, 1, 2, 3, 4, 5]
[3, 3, 3, 2, 2, 3, 4, 5]
[4, 4, 4, 3, 2, 3, 4, 5]
[5, 5, 5, 4, 3, 3, 4, 5]
[6, 6, 6, 5, 4, 4, 3, 4]
[7, 7, 7, 6, 5, 5, 4, 4]
[8, 7, 8, 7, 6, 6, 5, 5]						
"""

s1 = input()
s2 = input()
print(levenshteinDistance(s1, s2))
