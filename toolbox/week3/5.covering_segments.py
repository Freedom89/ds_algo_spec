# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple("Segment", "start end")


def optimal_points(segments):
    # remember, we need to sort by the end because the end is what captures it
    points = sorted(segments, key=lambda x: x.end)
    Rset = []
    i = 0
    n = len(segments)
    # because this is python where the index starts from 0, i only runs until n-1
    while i < n:
        # append the first element, the first element is always a segment
        current_segment = points[i]
        Rset.append(current_segment)
        i += 1  # jump to the next range
        # if the next segment starting point
        # is less than the current segment end point
        # jump to the next element again
        while i < n and points[i].start <= current_segment.end:
            i += 1

    # The assignment is only interested in the end point of each segment
    return [x.end for x in Rset]


input = "4 4 7 1 3 2 5 5 6"

if __name__ == "__main__":
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
