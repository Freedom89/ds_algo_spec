# Uses python3
import numpy as np

weight_limit, _ = [int(x) for x in input().split(" ")]
items = [int(x) for x in input().split(" ")]
items_tuple = [(x, x) for x in items]


def get_matrix(weight_limit, items_list):
    n_cols = weight_limit
    n_items = len(items_list)
    matrix = np.zeros((n_items + 1, n_cols + 1))

    for item_index in range(1, n_items + 1):
        for weight_index in range(1, n_cols + 1):
            # init by assuming that the most optimal choice is same as the previous choice
            # i.e no item is added since 2 items is optimal already
            matrix[item_index, weight_index] = matrix[item_index - 1, weight_index]
            # Get the current item and attributes
            current_item_weight, current_item_value = items_list[item_index - 1]
            # if the current item is less than the weight treshold,
            if current_item_weight <= weight_index:
                # get the index without the weight in the previous row
                # e.g in the 3rd row, go to the 2nd row and pick the corresponding index
                val = (
                    matrix[item_index - 1, weight_index - current_item_weight]
                    + current_item_value
                )
                # if the new value is better, assign to new value instead
                if matrix[item_index, weight_index] < val:
                    matrix[item_index, weight_index] = val
    return int(matrix[-1][-1])


print(get_matrix(weight_limit, items_tuple))