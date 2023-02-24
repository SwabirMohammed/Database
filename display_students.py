from main import Student

mystudents = Student.select()
for student in mystudents:
    print(student.student_name, student.student_id, student.student_class)