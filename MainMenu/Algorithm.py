def merge_sort(data, col_index, key=None):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]

    left_half = merge_sort(left_half, col_index, key=key)
    right_half = merge_sort(right_half, col_index, key=key)

    return merge(left_half, right_half, col_index, key=key)

def merge(left, right, col_index, key=None):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        left_item = left[i][col_index]
        right_item = right[j][col_index]

        if key:
            left_item = key(left_item)
            right_item = key(right_item)

        if left_item <= right_item:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(data, col_index, key=None):
    if len(data) <= 1:
        return data

    pivot = data[len(data) // 2][col_index]
    left = [row for row in data if int(row[col_index]) < int(pivot)]
    middle = [row for row in data if int(row[col_index]) == int(pivot)]
    right = [row for row in data if int(row[col_index]) > int(pivot)]

    if key:
        left = quick_sort(left, col_index, key=key)
        right = quick_sort(right, col_index, key=key)

    return left + middle + right


def bubble_sort(data, col_index, key = None):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][col_index] > data[j+1][col_index]:
                data[j], data[j+1] = data[j+1], data[j]
    return data