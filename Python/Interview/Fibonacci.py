def fibonacci_generator(limit):
    """Generates Fibonacci numbers up to a specified limit."""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# Example of using the generator:
for number in fibonacci_generator(50):
    print(number)

# second nth term

num = 5
a, b = 0, 1

for i in range(1,num):
    c = a + b
    a = b
    b = c
    print(c, end=" ")

# third

num = 5
a, b = 0, 1
while a <= num:
    print(a, end=" ")
    a, b = b, a + b

# fourth

num = 5
a, b = 0, 1
for i in range(num):
    print(a, end=" ")
    a,b=b,a+b

# fifth

def fib_fast(n):
    if n <= 0: return 0
    if n == 1: return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    # Works instantly even if input list contains numbers like 100 or 1000
    numbers = list(map(int, input().split()))
    results = [fib_fast(num) for num in numbers]
    print(*(results))

