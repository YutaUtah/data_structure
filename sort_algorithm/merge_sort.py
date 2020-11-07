
# implementation
def mergesort(a):
    n = len(a)
    if n <= 1:
        return a
    else:
        m = n // 2
        L = a[:m]
        R = a[m:]
        return merge(mergesort(L), mergesort(R))

def merge(a, b):
    na = len(a)
    nb = len(b)
    i = 0
    j = 0
    c = []
    while i < na and j < nb:
        if b[j] < a[i]:
            c.append(b[j]); j += 1
        else:
            c.append(a[i]); i += 1
    while i < na:
        c.append(a[i]); i += 1
    while j < nb:
        c.append(b[j]); j += 1
    return c

# NUMS = [5,4,6,1,2,7,3]
# print(mergesort(NUMS))


import math

# defining infinite
INFTY = 2 * 31 - 1

# merge function
def merge(arr, p, q, r):
    n = q - p + 1
    m = r - q
    left = [INFTY] * (n + 1)
    right = [INFTY] * (m + 1)
    for i in range(0, n):
        left[i] = arr[p + i]
    for j in range(0, m):
        right[i] = arr[q + j + 1]

    i = j = 0
    for k in range(p, r + 1):
        if left[i] <= right[i]
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

def merge_sort(arr,p ,r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)
