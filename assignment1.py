# Q) Practical Assignment - DPLMS Student Registration System
# 1. Display the message: 'Welcome to DPLMS Student Registration System'. 
# 2. Create a list containing these courses: Python with AI/ML, JavaScript, Flutter, and MERN Stack. 
# 3. Use a for loop to display all available courses. 
# 4. Ask the user to enter Student Name, Email, Age, and Selected Course. 
# 5. Store the entered information inside a Python dictionary. 
# 6. Use an if...else statement to check whether the selected course exists in the course list. 
# 7. If the course exists, display 'Registration Successful!'; otherwise display 'Course Not Available.' 8. Print the student's registration details in a clean, formatted output.



print("Welcome to DPLMS Student Registration System.")

courses = ["Python with AI/ML","JavaScript","Flutter","MERN Stack"]

print("Available Courses:")
for course in courses:
    print(course)

name = input("\nEnter Student Name:")
email = input("Enter Email:")
age = input("Enter Age:")
selected_course = input("Enter Selected Course:")

student = {
    "Name":name,
    "Email":email,
    "Age":age,
    "Selected Course":selected_course
}

if selected_course in courses:
    print("Registration Successful!")
else:
    print("Course Not Available.")

print("\nStudent Registration Details")
print("Name:",student["Name"])
print("Email:",student["Email"])
print("Age:",student["Age"])
print("Selected Course:",student["Selected Course"])