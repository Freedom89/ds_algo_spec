# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    num_stops = len(stops)
    stops = [0] + stops + [distance]  # add starting point and final stop
    num_refills = 0
    current_refill = 0
    while current_refill <= num_stops:
        last_refill = current_refill
        while (current_refill <= num_stops) and (
            stops[current_refill + 1] - stops[last_refill]
        ) <= tank:
            current_refill += 1
        if current_refill == last_refill:
            return -1
        if current_refill <= num_stops:
            num_refills += 1
    return num_refills


# compute_min_refills(950, 400, [200, 375, 550, 750])
# compute_min_refills(10, 3, [1, 2, 5, 9])
# compute_min_refills(200, 250, [100,150])

if __name__ == "__main__":
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
