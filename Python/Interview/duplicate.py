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
