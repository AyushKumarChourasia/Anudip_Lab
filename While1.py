# Input from user
number = int(input("Enter a number to reverse: "))

# Initialize reversed number
reversed_number = 0

num = number

# Reverse the number using a while loop
while num > 0:
    # Get the last digit of the number
    digit = num % 10
    # Add the digit to the reversed number
    reversed_number = (reversed_number * 10) + digit
    # Remove the last digit from the number
    num = num // 10

# Output the result
print(f"The reversed number is: {reversed_number}")
