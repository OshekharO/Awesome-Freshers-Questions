def sum_of_digits(n):
    total = 0
    for i in str(n):
        total += int(i)
    return total

print(sum_of_digits(123))

# 2nd Converts an integer into a list of its individual digits

num = 123
li = []

for i in str(num):
    li.append(int(i))

print(li)

total = 0

for i in li:
    total += i
    
print(total)
