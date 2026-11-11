# Valid Anagram: Check if two strings contain the same characters with the same frequencies.
# Example: s = "listen", t = "silent" -> True; s = "rat", t = "car" -> False

# Method 1: Using sorted()
def is_anagram_sort(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

s1, t1 = "anagram", "nagaram"
print("Method 1 (Sorted):", is_anagram_sort(s1, t1))


# 2nd Method: Using collections.Counter
from collections import Counter

def is_anagram_counter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

print("Method 2 (Counter):", is_anagram_counter("listen", "silent"))


# 3rd Method: Using a manual Hash Map (dict) - O(N) time, O(1) space (alphabet size)
def is_anagram_dict(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1

    return True

print("Method 3 (Dict):", is_anagram_dict("triangle", "integral"))


# 4th Method: Fixed array for ASCII characters
def is_anagram_ascii(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts = [0] * 26
    for c1, c2 in zip(s, t):
        counts[ord(c1) - ord('a')] += 1
        counts[ord(c2) - ord('a')] -= 1

    return all(c == 0 for c in counts)

print("Method 4 (ASCII array):", is_anagram_ascii("rat", "car"))
