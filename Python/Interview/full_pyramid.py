def print_full_pyramid(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")
        
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        
        print() # Move to the next line after each row

# Example usage:
num_rows = 5
print_full_pyramid(num_rows)
