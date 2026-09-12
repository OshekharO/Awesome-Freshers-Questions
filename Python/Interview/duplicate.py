s = ["a","b","c","c"]

for c in s:
    if s.count(c) > 1:
        print(c)

#2nd Method

s = ["a","b","c","c"]
dupli = []
seen = []

for letter in s:
    if letter in seen:
        dupli.append(letter)
    else:
        seen.append(letter)

print(dupli)

#3rd Method

sting = "hello"
seen = ""
dupli = ""

for i in sting:
    if i in seen:
        dupli = dupli + i
    else:
        seen = seen + i

print(seen)

#4th

string = "ProminentPixel"
seen = set()
duplicates = set()

for char in string:
    if char in seen:
        duplicates.add(char)
    else:
        seen.add(char)

print("Duplicate characters:", list(duplicates))

# Join with no space
print("".join(duplicates))

#5th

# Define the original array with duplicates
original_array = [1, 2, 2, 3, 4, 4, 5, 1, 6]

# Remove duplicates while keeping the original order
unique_array = list(dict.fromkeys(original_array))

# Print the result
print("Array after removing duplicates:", unique_array)

# Print 1st Unique Char From String

string = "swiss"
seen = set()
duplicates = set()

for char in string:
    if char in seen:
        duplicates.add(char)
    else:
        seen.add(char)

for i in string:
  if i not in duplicates:
    print(i)
    break;
