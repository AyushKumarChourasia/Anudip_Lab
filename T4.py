# Define the employee tuples
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# Create a list of employees
employees = [employee1, employee2, employee3]

# Iterate over the tuples and print the details
for employee in employees:
    print(f"Name: {employee[0]}, ID: {employee[1]}, Department: {employee[2]}, Salary: {employee[3]}")