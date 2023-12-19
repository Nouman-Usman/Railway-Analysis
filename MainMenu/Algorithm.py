from datetime import datetime

def merge_sort(data, col_index):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]

    left_half = merge_sort(left_half, col_index)
    right_half = merge_sort(right_half, col_index)

    return merge(left_half, right_half, col_index)

def merge(left, right, col_index):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][col_index] <= right[j][col_index]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Custom sorting function for time column
def custom_sort_time(arr):
    return sorted(arr, key=lambda x: datetime.strptime(x, "%I:%M %p"))

# Assuming 'quick_sort' function in your Algorithm.py
def quick_sort(arr, col_index):
    if len(arr) <= 1:
        return arr

    if col_index == 1:  # Assuming column 1 is the "Time" column
        return custom_sort_time(arr)
    elif col_index == 2:  # Assuming column 2 is the "Seats" column
        return quick_sort_seats(arr)

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left, col_index) + middle + quick_sort(right, col_index)

def quick_sort_seats(arr):
    return sorted(arr, key=lambda x: int(x))