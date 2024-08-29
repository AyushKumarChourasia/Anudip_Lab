marks = int(input("Enter marks: "))
# evaluating grade
if marks >= 80:
    grade = 'A'
elif 60 <= marks < 80:
    grade = 'B'
elif 50 <= marks < 60:
    grade = 'C'
elif 45 <= marks < 50:
    grade = 'D'
elif 25 <= marks < 45:
    grade = 'E'
elif marks < 25:
    grade = 'F'
else:
    grade = 'Invalid marks'
# print the grade
print(f"The corresponding grade is: {grade}")