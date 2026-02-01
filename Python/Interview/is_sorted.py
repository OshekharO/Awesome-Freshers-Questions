def is_sorted_iterative(arr):
  """Checks if a list is sorted in ascending order using iteration."""
  # Iterate from the second element (index 1) to the end
  for i in range(1, len(arr)):
    # If the current element is smaller than the previous one, it's unsorted
    if arr[i] < arr[i-1]:
      return False
  return True # If the loop completes, the list is sorted

# Example Usage:
list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 2, 4, 5]

print(f"{list1}: {is_sorted_iterative(list1)}") # Output: [1, 2, 3, 4, 5]: True
print(f"{list2}: {is_sorted_iterative(list2)}") # Output: [1, 3, 2, 4, 5]: False

## 2nd method

lint = [2,1,5,7,8]
link = [1,2,3,4,5]

for i in range(1, len(lint)):
    if lint[i] < lint[i - 1]:
        print("not sorted")
        break
    print("sorted")
    break
