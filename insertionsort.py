
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted into the sorted subarray
        j = i - 1

        # Move elements of the sorted subarray that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key into the sorted subarray
        arr[j + 1] = key


# Example usage:
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    insertion_sort(arr)
    print("Sorted array:", arr)


## O(n) - Linear time complexity
## O(n^2) - Quadratic time a^2

# Explanation:
#
# General Complexity and Efficiency of the Algorithm:
#
# Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It works by
# repeatedly taking an element from the unsorted part and inserting it into its correct position within the sorted
# part of the array. In the worst case, when the input array is in reverse order, it has a time complexity of O(n^2),
# where "n" is the number of elements in the array. In the best case, when the array is already sorted, it has a time
# complexity of O(n) because it only needs to perform comparisons without actual swaps. Its space complexity is O(1)
# because it only requires a constant amount of additional space for temporary variables.
#
# Runtime in Big O Notation:
#
# The runtime complexity of Insertion Sort is denoted as O(n^2) in the worst-case scenario, which is a quadratic time
# complexity. In the best-case scenario, where the array is already sorted, the runtime complexity is O(n),
# which is linear. Complexity Classification for the Algorithm:
#
# Insertion Sort is classified as an "elementary" sorting algorithm. It is straightforward to implement and is often
# used for small data sets or when the array is nearly sorted. While it is not the most efficient sorting algorithm
# for large data sets (due to its quadratic time complexity), it can be efficient for small arrays or as part of more
# complex sorting algorithms like Timsort, which uses a combination of Insertion Sort and Merge Sort to achieve
# better performance.
