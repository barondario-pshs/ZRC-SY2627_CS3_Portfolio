class Student:
    def __init__(self, name, student_id):
        self.name = name
        self._student_id = student_id

class Course:
    def __init__(self, course_name, professor):
        self.course_name = course_name
        self._professor = professor
        self.students = []

    def add_student(self, student: Student):
        """"Appends a Student object to the course's student list."""
        self.students.append(student)
