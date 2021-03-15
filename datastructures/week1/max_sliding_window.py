# python3


# m, n = 4, 8
# sequence = [int(x) for x in "2 7 3 1 5 2 6 2".split()]
# max_sliding_window_naive(sequence, 4)


# sequence = [int(x) for x in "6 5 4 3 2 1".split()]
# max_sliding_window_naive(sequence, 2)
# # m = 2
# # n = 6

# sequence = [
#     int(x)
#     for x in "15323 48315 55723 74656 43007 42022 67451 95562 24360 79353 14333 8765 95854 39022 84651 70067 63147 21636 18826 32119 4310 7782 89005 57922 73772 4972 64687 17424 45146 55189 68373 1792 90512 5328 55884 54501 68792 18531 30966 34136 11209 72209 456 12554 38031 68807 50862 34335 60966 50689 59632 68240 22709 26625 41486 78071 84979 98660 85510 67525".split()
# ]
# m = 20
# max_sliding_window_naive(sequence, 20)


def max_sliding_window_naive(sequence, m):
    n = len(sequence)
    current_sequence = []
    tracker_sequence = []
    current_max = 0
    # init the first set of sequence
    for current_number in sequence[0:m]:
        current_max = max(current_number, current_max)
        current_sequence.append(current_number)
    # This is the first maximum
    maximums = [current_max]
    # This is using hint 3 in the notes
    # Only concern about max numbers, and in order of numbers appearing after max
    # in the initial sequence
    max_index = current_sequence.index(current_max)
    tracker_sequence = sorted(current_sequence[max_index:], key=lambda x: -x)[0:m]
    for current_number in sequence[m:n]:
        while True:
            # if the current number is greater than the max,
            # destory everything
            if current_number > current_max:
                current_max = current_number
                tracker_sequence = [current_number]
                break
            # Otherwise,clean up all numbers that is smaller than the new comer
            if tracker_sequence[-1] < current_number:
                tracker_sequence.pop()
            else:
                # After cleaning up, add the new comer
                tracker_sequence.append(current_number)
                break
        # If the number that is leaving the current sequence
        # is the current maximum, get rid of it from the tracker
        # and take the second in line in the tracker
        if current_sequence[0] == current_max:
            tracker_sequence.pop(0)
            current_max = tracker_sequence[0]
        # remove the sequence, add the sequence
        # You need this step to keep track of current_sequence[0]
        current_sequence.pop(0)
        current_sequence.append(current_number)
        # print(current_sequence, tracker_sequence, current_max)
        maximums.append(current_max)
    return maximums


if __name__ == "__main__":
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))
