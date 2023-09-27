def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the sorted elements back to the original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_element = max(arr)
    exp = 1
    while max_element // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# 1. Understanding: Radix Sort is a non-comparative sorting algorithm that works by distributing elements into
# different "buckets" based on their digits or position. It sorts numbers by processing individual digits from the
# least significant digit (LSD) to the most significant digit (MSD) or vice versa.
#
# 2. Big O Notation: The runtime efficiency of Radix Sort is O(k * n), where "n" is the number of elements to be
# sorted, and "k" is the number of digits in the maximum number in the list.
#
# 3. Complexity Classification:
#
# Time Complexity: O(k * n) - linear time complexity for integer sorting.
# Space Complexity: O(n + k) - linear space complexity for storing the buckets.
