# # try to implement this on your own

from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j],  numbers[j+1] =  numbers[j+1],  numbers[j]

    return numbers


if __name__ == "__main__":
    nums = [2,5,1,8,7,3]
    print(bubble_sort(nums))

def bubble(arr, n):
    for i in range(0, n-1):
        for j in range(n-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

arr = [5,9,2,1,7,3,4,6,8,0]
bubble(arr, len(arr))
print(arr)