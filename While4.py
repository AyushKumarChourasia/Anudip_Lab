# Initialize the sum
total_sum = 0

# Infinite loop to accept input
while True:
    # Input from user
    number = int(input("Enter any number ( Enter 0 to stop): "))
    
    # Check if the input is 0
    if number == 0:
        break
    
    # Add the number to the total sum
    total_sum += number

# Output the result
print(f"The sum of all numbers entered is: {total_sum}")
