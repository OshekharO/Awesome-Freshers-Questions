#Given a string, return a string containing only the characters that appear exactly once

from collections import Counter

def unique_characters(s: str) -> str:
    # Count occurrences of each character
    char_counts = Counter(s)
    
    # Filter and join characters that appear exactly once
    return "".join(char for char in s if char_counts[char] == 1)

# Example usage:
print(unique_characters("swiss"))    # Output: "wri" (s appears 3 times)
print(unique_characters("racecar"))  # Output: "e"
