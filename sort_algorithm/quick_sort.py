def partition(A, start, end):
    pivot = A[end]
    i = start - 1
    for j in range(start, end):
        if A[j] <= pivot:
            # A[i+1]の要素はピボットより大きい要素なので
            # A[i+1]とピボット以下の大きさの要素A[j]の位置を入れ替える
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[end] = A[end], A[i + 1]
    print(A)
    return i + 1


def quicksort(A, start, end):
    if start < end:
        pivot_position = partition(A, start, end)
        quicksort(A, start, pivot_position - 1)
        quicksort(A, pivot_position + 1, end)


if __name__ == "__main__":
    A = [1, 3, 8, 2, 4, 9, 5, 10, 7, 6]
    print(A)
    quicksort(A, 0, len(A)-1)
    print(A)


# def partition(numbers, low, high):
#     i = low - 1
#     pivot = numbers[high]
#     for j in range(low, high):
#         if numbers[j] <= pivot:
#             i += 1
#             numbers[i], numbers[j] = numbers[j], numbers[i]
#     numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
#
#     # return the index number of the pivot
#     return i+1
#
#
# def quick_sort(numbers):
#     def _quick_sort(numbers, low, high):
#         if low < high:
#             partition_index = partition(numbers, low, high)
#             _quick_sort(numbers, low, partition_index-1)
#             _quick_sort(numbers, partition_index+1, high)
#
#     _quick_sort(numbers, 0, len(numbers)-1)
#     return numbers
#
#     # partition(numbers, low, high)
#
#
#
#
# if __name__ == '__main__':
#     nums = [1,8,3,9,4,5,7]
#     print(quick_sort(nums))
