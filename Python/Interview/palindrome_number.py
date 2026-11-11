# Palindrome Number: Check if an integer is a palindrome (without converting to string where possible)
# Example: 121 -> True, -121 -> False, 10 -> False

# Method 1: String Conversion (Pythonic & Simple)
def is_palindrome_num_str(x: int) -> bool:
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]

print("Method 1 (String):", is_palindrome_num_str(121))
print("Method 1 (Negative):", is_palindrome_num_str(-121))


# 2nd Method: Mathematical Full Integer Reversal (No String Conversion)
def is_palindrome_num_math(x: int) -> bool:
    if x < 0:
        return False
    original = x
    reversed_num = 0
    while x > 0:
        reversed_num = (reversed_num * 10) + (x % 10)
        x //= 10
    return original == reversed_num

print("Method 2 (Math Full):", is_palindrome_num_math(12321))


# 3rd Method: Mathematical Half Reversal (Optimal - Prevents Integer Overflow Risk)
def is_palindrome_num_half(x: int) -> bool:
    # If negative or ends with 0 (except 0 itself), cannot be a palindrome
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = (reversed_half * 10) + (x % 10)
        x //= 10

    # For even length: x == reversed_half
    # For odd length: x == reversed_half // 10 (middle digit discarded)
    return x == reversed_half or x == (reversed_half // 10)

print("Method 3 (Math Half):", is_palindrome_num_half(1221))
print("Method 3 (Math Half False):", is_palindrome_num_half(10))
