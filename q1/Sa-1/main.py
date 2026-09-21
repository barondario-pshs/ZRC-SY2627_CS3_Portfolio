class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date, is_submitted, grade, submitted_files):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = bool(is_submitted)
        self.__grade = float(grade)
        self.__submitted_files = list(submitted_files)

    # Private Methods (-)
    def __validate_grade(self, score: float) -> bool:
        """Validate if the grade is within the acceptable range (0-100)."""
        return 0 <= score <= 100

    def __check_submission_status(self) -> bool:
        """Check if the assignment has been submitted."""
        return self.__is_submitted

    def __is_duplicate_file(self, file_name: str) -> bool:
        """Check if the submitted file is a duplicate."""
        return file_name in self.__submitted_files

    # Public Methods (+)
    def add_file(self, file_name:str):
        if not self.__is_duplicate_file(file_name):
            self.__submitted_files.append(file_name)
            print(f"File '{file_name}' added successfully.")

    def remove_file(self, file_name: str) -> None:
        if file_name in self.__submitted_files:
            self.__submitted_files.remove(file_name)
            print(f"File '{file_name}' removed successfully.")
        else:
            print(f"File '{file_name}' not found in the submission.")

    def assign_grade(self, score: float) -> None:
        if self.__validate_grade(score):
            self.__grade = score
            print(f"Grade assigned: {score}")
        else:
            print("Invalid grade. Please enter a value between 0 and 100.")

    def get_grade(self) -> str:
        return str(self.__grade)

    def view_files(self) -> str:
        return ", ".join(self.__submitted_files)

    def get_status_report(self) -> str:
        status = "Submitted" if self.__check_submission_status() else "Not Submitted"
        return f"Assignment: {self._assignment_title}, Status: {status}, Grade: {self.__grade}"


# Object Instantation

student1 = AssignmentSubmission(
    student_name="Alex Gonzaga",
    student_id="pshs-1090",
    assignment_title="CS-101",
    due_date="2024-10-01",
    is_submitted=False,
    grade=0.0,
    submitted_files=[]
)

student2 = AssignmentSubmission(
    student_name="Adelle",
    student_id="pshs-1920-x",
    assignment_title="CS-103",
    due_date="2026-10-01",
    is_submitted=False,
    grade=0.0,
    submitted_files=[]
)

student3 = AssignmentSubmission(
    student_name="Jay One",
    student_id="pshs-1234",
    assignment_title="CS-104",
    due_date="2026-10-01",
    is_submitted=False,
    grade=0.0,
    submitted_files=[]
)

student4 = AssignmentSubmission(
    student_name="Blinet",
    student_id="pshs-5678",
    assignment_title="CS-105",
    due_date="2026-10-01",
    is_submitted=False,
    grade=0.0,
    submitted_files=[]
)

student5 = AssignmentSubmission(
    student_name="Jean",
    student_id="pshs-0202",
    assignment_title="CS-106",
    due_date="2026-10-01",
    is_submitted=False,
    grade=0.0,
    submitted_files=[]
)

#printprintprint

print("\n---TEST SCENARIO 1: Multiple Files via List---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95.0)
print(f"Alex's Files: {student1.view_files()}")

print("\n---TEST SCENARIO 2: Removing Files from List---\n")
student2.add_file("wrong_homework.docx")
student2.remove_file("homework.docx")  
student2.add_file("correct_project.py")
student2.assign_grade(88.0)
print(f"Adelle's Files: {student2.view_files()}")

print("\n---TEST SCENARIO 3: Preventing Duplicate Files---\n")
student3.add_file("script.py")
student3.add_file("script.py")
print(f"Jay's Files: {student3.view_files()}")

print("\n---TEST SCENARIO 4: Removing file after being graded---\n")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75.0)
student4.remove_file("exam_answers.pdf")
print()

print("\n---TEST SCENARIO 5: Empty List Handling---\n")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100.0)
print()

print("\n--- FINAL SYSTEM REPORT ---\n")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
