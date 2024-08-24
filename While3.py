# Input from user
number = int(input("Enter a number to find its factorial: "))

# Initialize factorial result
factorial = 1

# Copy of the original number to manipulate
num = number

# Calculate factorial using a while loop
while num > 0:
    factorial *= num
    num -= 1

# Output the result
print(f"The factorial of {number} is: {factorial}")
