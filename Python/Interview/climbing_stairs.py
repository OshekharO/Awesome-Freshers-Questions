# Climbing Stairs: Each time you can climb 1 or 2 steps. How many distinct ways can you climb n steps?
# Example: n = 2 -> 2 (1+1, 2)
# Example: n = 3 -> 3 (1+1+1, 1+2, 2+1)
# Example: n = 4 -> 5

# Method 1: Space-Optimized Iterative (Fibonacci Pattern) - O(N) Time, O(1) Space
def climb_stairs_iterative(n: int) -> int:
    if n <= 2:
        return n
    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second

print("Method 1 (Space-Optimized O(1)):", climb_stairs_iterative(5))


# 2nd Method: Dynamic Programming Array - O(N) Time, O(N) Space
def climb_stairs_dp(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print("Method 2 (DP Table):", climb_stairs_dp(5))


# 3rd Method: Recursion with Memoization (Top-Down)
def climb_stairs_memo(n: int, memo=None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return n
    memo[n] = climb_stairs_memo(n - 1, memo) + climb_stairs_memo(n - 2, memo)
    return memo[n]

print("Method 3 (Memoization):", climb_stairs_memo(5))
