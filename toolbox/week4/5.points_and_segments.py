# https://www.coursera.org/learn/algorithmic-toolbox/discussions/weeks/4/threads/QJ1jK9wNEeWdPBL2iFTrAw/replies/Ihiw4txhEeWK5g7mfcS2Xw/comments/oyAMaeIiEeWyqwpvChh66Q?page=2

"""
explanation of the problem
2 3 
0 5 
7 10 
1 6 11 
1 -> inside 0 5 
6 -> not inside anything
11 -> not inside anything
"""

master_list = list()
s, p = [int(i) for i in input().split()]

for i in range(s):
    a, b = [int(i) for i in input().split()]
    master_list.append((a, "l"))
    master_list.append((b, "r"))

points = input().split()
for i in points:
    master_list.append((int(i), "p"))

# s = 2
# p = 3
# master_list = [(0, 'l'), (5, 'r'), (7, 'l'), (10, 'r'), (1, 'p'), (6, 'p'), (11, 'p')]

master_list.sort()

segment_count = 0
point_segment_map = dict()
for i in master_list:
    if i[1] == "l":
        segment_count += 1
    # any points to the left
    elif i[1] == "r":
        segment_count -= 1
    else:
        # for the current point, since it is between x segments,
        # it get x segment_count points
        point_segment_map[i[0]] = segment_count

temp = ""
for i in points:
    temp += str(point_segment_map[int(i)]) + " "
print(temp[:-1])