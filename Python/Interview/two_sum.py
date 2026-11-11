# Two Sum: Given an array of integers and an integer target,
# return indices of the two numbers such that they add up to target.
# Example: nums = [2, 7, 11, 15], target = 9 -> [0, 1]

# Method 1: Brute Force O(N^2)
def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print("Method 1 (Brute):", two_sum_brute([2, 7, 11, 15], 9))


# 2nd Method: One-Pass Hash Map (Dictionary) - O(N) Time, O(N) Space
def two_sum_hashmap(nums, target):
    seen = {}  # maps number to its index
    for index, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
    return []

print("Method 2 (Hash Map):", two_sum_hashmap([3, 2, 4], 6))


# 3rd Method: Two Pointers (when array is sorted or with indexed tuples)
def two_sum_two_pointers(nums, target):
    # Store value with original index
    indexed_nums = sorted([(num, idx) for idx, num in enumerate(nums)])
    left = 0
    right = len(indexed_nums) - 1

    while left < right:
        curr_sum = indexed_nums[left][0] + indexed_nums[right][0]
        if curr_sum == target:
            return [indexed_nums[left][1], indexed_nums[right][1]]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return []

print("Method 3 (Two Pointers):", two_sum_two_pointers([1, 5, 2, 7, 4], 9))
