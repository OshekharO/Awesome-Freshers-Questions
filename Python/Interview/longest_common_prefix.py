# Longest Common Prefix: Find the longest common prefix string amongst an array of strings.
# Example: ["flower","flow","flight"] -> "fl"
# Example: ["dog","racecar","car"] -> ""

# Method 1: Horizontal Scanning
def longest_common_prefix_horizontal(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

print("Method 1 (Horizontal):", longest_common_prefix_horizontal(["flower", "flow", "flight"]))


# 2nd Method: Vertical Scanning (Compare character by character across strings)
def longest_common_prefix_vertical(strs):
    if not strs:
        return ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]
    return strs[0]

print("Method 2 (Vertical):", longest_common_prefix_vertical(["interspecies", "interstellar", "interstate"]))


# 3rd Method: Lexicographical Sorting (Compare first and last after sorting)
def longest_common_prefix_sort(strs):
    if not strs:
        return ""
    strs = sorted(strs)
    first, last = strs[0], strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    return first[:i]

print("Method 3 (Sorted):", longest_common_prefix_sort(["throne", "throne", "throne"]))
