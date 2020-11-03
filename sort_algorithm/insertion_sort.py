# from typing import List
#
# def insertion_sort(numbers: List[int]) -> List[int]:
#     len_numbers = len(numbers)
#     for i in range(1, len_numbers):
#         temp = numbers[i]
#         j = i - 1
#         while j >= 0 and numbers[j]>temp:
#             numbers[j+1] = numbers[j]
#             j -= 1
#         numbers[j+1] = temp
#
#     return numbers
#
# if __name__ == '__main__':
#     nums = [1,7,3,2,8,5]
#     print(insertion_sort(nums))

def insertion(arr, n):
    for i in range(1, n):
        val = arr[i] # temporary value to sort 

        j = i - 1
        while j >= 0 and arr[j] > val:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val

arr = [5,9,2,1,7,3,4,6,8,0]
insertion(arr, len(arr))
print(arr)