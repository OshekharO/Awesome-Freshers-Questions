# First Unique Character in a String:
# Given a string s, find the first non-repeating character and return its index. If none, return -1.
# Example: s = "leetcode" -> 0; s = "loveleetcode" -> 2; s = "aabb" -> -1

# Method 1: Hash Map / Dict Two-Pass - O(N) Time, O(1) Space
def first_uniq_char_dict(s: str) -> int:
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for index, char in enumerate(s):
        if counts[char] == 1:
            return index
    return -1

print("Method 1 (Dict):", first_uniq_char_dict("leetcode"))


# 2nd Method: collections.Counter
from collections import Counter

def first_uniq_char_counter(s: str) -> int:
    char_counts = Counter(s)
    for index, char in enumerate(s):
        if char_counts[char] == 1:
            return index
    return -1

print("Method 2 (Counter):", first_uniq_char_counter("loveleetcode"))


# 3rd Method: Using str.find() and str.rfind()
def first_uniq_char_find(s: str) -> int:
    for index, char in enumerate(s):
        if s.find(char) == s.rfind(char):
            return index
    return -1

print("Method 3 (find == rfind):", first_uniq_char_find("aabb"))
