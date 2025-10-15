def is_palindrome(s):
  s = s.lower()
  # Compare the original string with its reverse
  return s == s[::-1]

# Example usage:
string1 = "madam"
string2 = "hello"
string3 = "Racecar"

print(f"'{string1}' is a palindrome: {is_palindrome(string1)}")
print(f"'{string2}' is a palindrome: {is_palindrome(string2)}")
print(f"'{string3}' is a palindrome: {is_palindrome(string3)}")

# Second

s = "geeks"
rev = ''.join(reversed(s))

if s == rev:
    print("Yes")
else:
    print("No")

# third

s = "malayalam"
rev = ""  # store the reversed string

for char in s:
    rev = char + rev

if s == rev:
    print("Yes")
else:
    print("No")
