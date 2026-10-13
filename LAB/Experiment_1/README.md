Aim
To implement the Merge Sort algorithm using the Divide and Conquer technique and calculate its time complexity.

1. Algorithm / Procedure
Algorithm: Merge Sort
Step 1: Start.

Step 2: Read the array of n elements.

Step 3: Divide the array into two halves.

Step 4: Recursively apply Merge Sort to the left half.

Step 5: Recursively apply Merge Sort to the right half.

Step 6: Merge the two sorted halves by comparing their elements.

Step 7: Repeat the merging until the complete array is sorted.

Step 8: Display the sorted array.

Step 9: Stop.

2. Python Program
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Input
arr = list(map(int, input("Enter elements: ").split()))

# Sorting
sorted_arr = merge_sort(arr)

# Output
print("Sorted array:", sorted_arr)
3. Sample Result
Input
Enter elements: 38 12 27 43 9 31 18 25
Output
Sorted array: [9, 12, 18, 25, 27, 31, 38, 43]
Result
Thus, the given array was successfully sorted using the Merge Sort algorithm based on the Divide and Conquer technique.

4. Interface
Input Interface
Merge Sort successfully sorts the array using the Divide and Conquer technique.

5. Analysis
Best-case time complexity: O(n log n) Average-case time complexity: O(n log n) Worst-case time complexity: O(n log n) Space complexity: O(n) for this implementation.
