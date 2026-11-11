# Maximum Subarray (Kadane's Algorithm)
# Given an integer array nums, find the contiguous subarray with the largest sum and return its sum.
# Example: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> Output: 6 (Subarray: [4, -1, 2, 1])

# Method 1: Kadane's Algorithm - O(N) Time, O(1) Space (Optimal)
def max_sub_array_kadane(nums):
    max_so_far = nums[0]
    current_max = nums[0]

    for x in nums[1:]:
        current_max = max(x, current_max + x)
        max_so_far = max(max_so_far, current_max)

    return max_so_far

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Method 1 (Kadane):", max_sub_array_kadane(numbers))


# 2nd Method: Dynamic Programming Array - O(N) Time, O(N) Space
def max_sub_array_dp(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
    return max(dp)

print("Method 2 (DP Array):", max_sub_array_dp(numbers))


# 3rd Method: Brute Force O(N^2) (Conceptual baseline for interviews)
def max_sub_array_brute(nums):
    max_sum = float('-inf')
    n = len(nums)
    for i in range(n):
        curr = 0
        for j in range(i, n):
            curr += nums[j]
            if curr > max_sum:
                max_sum = curr
    return max_sum

print("Method 3 (Brute Force):", max_sub_array_brute([5, 4, -1, 7, 8]))
