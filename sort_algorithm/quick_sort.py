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