def sum_of_digits(n):
    total = 0
    for i in str(n):
        total += int(i)
    return total

print(sum_of_digits(123))
