def fibonacci_generator(limit):
    """Generates Fibonacci numbers up to a specified limit."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# Example of using the generator:
for number in fibonacci_generator(50):
    print(number)

# second

num = 5
a, b = 0, 1

for i in range(1,num):
    c = a + b
    a = b
    b = c
    print(c, end=" ")
