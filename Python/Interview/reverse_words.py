# Reverse Words in a String:
# Example: "  the sky   is blue  " -> "blue is sky the"

# Method 1: Pythonic split and reverse slicing
def reverse_words_pythonic(s: str) -> str:
    # split() without arguments automatically splits on arbitrary whitespace and strips leading/trailing
    words = s.split()
    return " ".join(words[::-1])

text = "  the sky   is blue  "
print("Method 1 (split + slice):", f"'{reverse_words_pythonic(text)}'")


# 2nd Method: Using reversed() iterator
def reverse_words_reversed(s: str) -> str:
    return " ".join(reversed(s.split()))

print("Method 2 (reversed):", f"'{reverse_words_reversed(text)}'")


# 3rd Method: Manual Two Pointers / Token extraction without split()
def reverse_words_manual(s: str) -> str:
    words = []
    i = 0
    n = len(s)

    while i < n:
        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1
        if i >= n:
            break

        # Find end of current word
        j = i
        while j < n and s[j] != ' ':
            j += 1

        words.append(s[i:j])
        i = j

    # Reverse words list in-place using two pointers
    left, right = 0, len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1

    return " ".join(words)

print("Method 3 (Manual parsing):", f"'{reverse_words_manual('  hello   world  ')}'")
