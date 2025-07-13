# ------------------ Task 2 ------------------
# Problem Statement:
# Write a Python program that:
# 1. Uses a for loop to iterate over numbers from 1 to 50.
# 2. Calculates the sum of all integers in this range.
# 3. Displays the final sum.

# Example Output:
# The sum of numbers from 1 to 50 is: 1275

# Solution:
total_sum = 0

for num in range(1, 51):
    total_sum += num

print("The sum of numbers from 1 to 50 is:", total_sum)
