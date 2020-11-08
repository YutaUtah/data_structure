def linear_search(nums, key):
    for i in range(0, len(nums)):
        if nums[i] == key:
            return i
    return None

if __name__ == '__main__':
    nums = [3,4,6,7,9,1,2]
    index = linear_search(nums, 7)
    print(index)