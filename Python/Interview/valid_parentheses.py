# Valid Parentheses: Determine if the input string has valid matching brackets.
# Bracket types: '()', '{}', '[]'
# Example: "()[]{}" -> True, "(]" -> False, "([)]" -> False, "{[]}" -> True

# Method 1: Using Stack - O(N) Time, O(N) Space (Optimal)
def is_valid_parentheses_stack(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            continue

    return len(stack) == 0

print("Method 1 (Stack):", is_valid_parentheses_stack("{[()]}"))
print("Method 1 (Stack invalid):", is_valid_parentheses_stack("([)]"))


# 2nd Method: String Replacement (Reduction) Loop
def is_valid_parentheses_replace(s: str) -> bool:
    # Continuously remove matching adjacent pairs
    prev_len = -1
    while len(s) != prev_len:
        prev_len = len(s)
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return len(s) == 0

print("Method 2 (String Replace):", is_valid_parentheses_replace("()[]{}"))
print("Method 2 (String Replace invalid):", is_valid_parentheses_replace("((("))
