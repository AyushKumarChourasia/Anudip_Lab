# Input from user
number = int(input("Enter a number to check if it is a palindrome: "))
original_number = number

# Initialize reversed number
reversed_number = 0

# Reverse the number
while number > 0:
    # Get the last digit of the number
    digit = number % 10
    # Add the digit to the reversed number
    reversed_number = (reversed_number * 10) + digit
    # Remove the last digit from the number
    number = number // 10

# Check if the original number and reversed number are the same
if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")
