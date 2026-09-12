numbers = [10, 20, 4, 45, 99, 99, 4]

second_largest = sorted(list(set(numbers)))[-2]
print(second_largest)

#2

def find_second_largest(arr):
    # An array must have at least two elements
    if len(arr) < 2:
        return None
    
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
            
    return second if second != float('-inf') else None

# Example usage:
nums = [12, 35, 1, 10, 34, 35, 1]
print(find_second_largest(nums))  # Output: 34
