""" Implementation to demonstrate memory management optimization can improve HPC. """
import numpy
import time

def in_place_reverse(arr):
    """ Function to reverse the elements in array using cache utilization. """
    start = 0
    end = len(arr) - 1
    while start < end:
        # Swap elements without creating new array
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

def new_array_reverse(arr):
    """ Function to reverse the elements in array by using new array. """
    reversed_arr = numpy.zeros_like(arr)  # Create a new array of the same size
    n = len(arr)
    for i in range(n):
        reversed_arr[i] = arr[n - 1 - i]  # Copy elements in reverse order
    return reversed_arr

# Generate a large random 1D array
size = 10000000
array = numpy.random.rand(size)

# Measure performance of in-place reversal (optimized)
start_time = time.time()
# Use numpy.copy to avoid modifying the original array
in_place_reversed = in_place_reverse(numpy.copy(array))
in_place_time = time.time() - start_time

# Measure performance of new array reversal (less efficient)
start_time = time.time()
new_array_reversed = new_array_reverse(array)
new_array_time = time.time() - start_time

# Output the performance results
print(f"In-Place Reversal Time (Optimized): {in_place_time:.4f} seconds")
print(f"New Array Reversal Time (Less Efficient): {new_array_time:.4f} seconds")