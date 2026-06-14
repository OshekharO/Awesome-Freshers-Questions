// Adding without using built in function or + operator

a = 5
b = 10
c = a & b
a = a ^ b
b = c << 1
print(b)

// Alternatively 

def get_sum(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a
