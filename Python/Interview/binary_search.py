# Binary Search: Search target in a sorted ascending array. Return index or -1 if not found.
# Example: nums = [-1, 0, 3, 5, 9, 12], target = 9 -> Output: 4

# Method 1: Iterative Two-Pointer - O(log N) Time, O(1) Space (Optimal)
def binary_search_iterative(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Prevents integer overflow in standard languages
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

nums = [-1, 0, 3, 5, 9, 12]
print("Method 1 (Iterative):", binary_search_iterative(nums, 9))


# 2nd Method: Recursive Binary Search - O(log N) Time, O(log N) Call Stack
def binary_search_recursive(nums, target, left, right):
    if left > right:
        return -1

    mid = left + (right - left) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)

print("Method 2 (Recursive):", binary_search_recursive(nums, 2, 0, len(nums) - 1))


# 3rd Method: Standard Library `bisect`
import bisect

def binary_search_bisect(nums, target):
    index = bisect.bisect_left(nums, target)
    if index < len(nums) and nums[index] == target:
        return index
    return -1

print("Method 3 (bisect):", binary_search_bisect(nums, 12))
