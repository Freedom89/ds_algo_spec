# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    output_value = 0.0
    unit_value = [dict(unit=v / w, weight=w, value=v) for w, v in zip(weights, values)]
    unit_value_sorted = sorted(unit_value, key=lambda x: -x.get("unit"))
    remaining_capacity = capacity
    counter = 0
    len_items = len(unit_value_sorted)
    while remaining_capacity > 0:
        current_item = unit_value_sorted[counter]
        # if the capacity is less than the current item, take all that is available
        if remaining_capacity < current_item.get("weight"):
            output_value += current_item.get("unit") * remaining_capacity
            remaining_capacity = 0
        # if the remaining capacity can contian the entire item, take the entire item
        elif remaining_capacity >= current_item.get("weight"):
            output_value += current_item.get("value")
            remaining_capacity -= current_item.get("weight")
        # if the counter exceeds the number of item, just finish the loop
        counter += 1
        if counter >= len_items:
            break
    return output_value


# def split_data(data: list):
#     n, capacity = data[0:2]
#     values = data[2 : (2 * n + 2) : 2]
#     weights = data[3 : (2 * n + 2) : 2]
#     return get_optimal_value(capacity, weights, values)


# split_data([3, 50, 60, 20, 100, 50, 120, 30])
# split_data([1, 10, 500, 30])

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
