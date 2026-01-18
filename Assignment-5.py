'''Task-1'''

#Create a Dictionary of Student Marks
student_marks = {'Alice': 85,'Bob': 92,'Charlie': 78,'Diana': 96,'Eve': 88}

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")

'''Task-2'''

# Demonstrate List Slicing

# Creating a list of numbers from 1 to 10
numbers = list(range(1, 11))
print(f"Original list: {numbers}")

# Extracting the first five elements using list slicing
first_five = numbers[:5]
print(f"Extracted first five elements: {first_five}")

# Reversing the extracted elements
reversed_first_five = first_five[::-1]
print(f"Reversed extracted elements: {reversed_first_five}")


















