num_rows = 5

for i in range(1, num_rows + 1):  # Outer loop for rows (1 to 5)
    for j in range(i):          # Inner loop for stars (prints 'i' stars)
        print("*", end="")
    print()                     # New line after each row
