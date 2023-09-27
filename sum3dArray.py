def sum_3d_array(arr):
    n = len(arr)
    total_sum = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                total_sum += arr[i][j][k]

    return total_sum


# Algorithm:

# Initialize a variable total_sum to 0 to store the sum of all values.
# Use three nested loops to iterate through each element in the 3D array:
# The outer loop iterates from 0 to n - 1.
# The middle loop iterates from 0 to n - 1.
# The inner loop iterates from 0 to n - 1.
# In the innermost loop, add the value of the current element to total_sum.
# After all loops complete, total_sum will contain the sum of all values in the 3D array.
# Complexity Analysis:
#
# Time Complexity (Big O Notation): O(n^3) - The algorithm iterates through all n^3 elements in the 3D array.
# Space Complexity: O(1) - The algorithm uses a constant amount of space.