from main import Student

try:
    student_name = input("Enter Student Name")
    student_id = input("Enter Student ID")
    student_class = input("Enter Student Class")

    Student.create(name=student_name, id=student_id, grade=student_class)
    print("Student registered successfully")

except:
    print("Failed to register student, use a different ID")