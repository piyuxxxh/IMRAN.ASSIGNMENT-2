# Assignment 2 - Control Structures in Python

# ------------------ Task 1 ------------------
# Problem Statement:
# Write a Python program that:
# 1. Takes an integer input from the user.
# 2. Checks whether the number is even or odd using an if-else statement.
# 3. Displays the result accordingly.

# Example Output:
# Enter a number: 7
# 7 is an odd number.

# Solution:
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"The number {number} is Even.")
else:
    print(f"The number {number} is Odd.")
