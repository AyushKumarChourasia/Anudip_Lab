# Define the list of tuples
tuples_list = [(1, 2), (3, 4), (5, 6)]

# Calculate the sum of the numbers in the tuple
total_sum = sum(sum(t) for t in tuples_list)

# Print the result
print("The sum of the numbers in the tuple is:", total_sum)
