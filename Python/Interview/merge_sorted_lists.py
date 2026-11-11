# Merge Two Sorted Lists: Combine two sorted lists into one sorted list.
# Example: list1 = [1, 2, 4], list2 = [1, 3, 4] -> [1, 1, 2, 3, 4, 4]

# Method 1: Concatenation and Sort - O((N+M) log(N+M))
def merge_sorted_builtin(l1, l2):
    return sorted(l1 + l2)

print("Method 1 (Concat + sort):", merge_sorted_builtin([1, 2, 4], [1, 3, 4]))


# 2nd Method: Two-Pointer Linear Merge - O(N + M) Time, O(N + M) Space
def merge_sorted_two_pointers(l1, l2):
    merged = []
    i = 0
    j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1

    # Append any remaining elements
    merged.extend(l1[i:])
    merged.extend(l2[j:])
    return merged

print("Method 2 (Two Pointers):", merge_sorted_two_pointers([1, 3, 5], [2, 4, 6, 8]))


# 3rd Method: Using heapq.merge (standard library generator) - O(N + M)
import heapq

def merge_sorted_heapq(l1, l2):
    return list(heapq.merge(l1, l2))

print("Method 3 (heapq.merge):", merge_sorted_heapq([5, 10, 15], [3, 8, 12]))
