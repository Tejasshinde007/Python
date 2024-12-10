class Student:
    def __init__(self, roll_no, name, grade):
        self.roll_no = roll_no
        self.name = name
        self.grade = grade
    
    def update_grade(self, new_grade):
        self.grade = new_grade
        
    def __str__(self):
        return f"Roll No: {self.roll_no}, Name: {self.name}, Grade: {self.grade}"
    
class School:
    def __init__(self):
        self.students = {}
        
    def add_student(self, roll_no, name, grade):
        if roll_no in self.students:
            print(f"Student with Roll No {roll_no} already exists!")
        else:
            self.students[roll_no] = Student(roll_no, name, grade)
            print(f"Student {name} (Roll No: {roll_no}) has been added successfully.")
    
    def remove_student(self, roll_no):
        if roll_no in self.students:
            removed_student = self.students.pop(roll_no)
            print(f"Student {removed_student.name} (Roll No: {roll_no}) removed successfully.")
        else:
            print(f"Student with Roll No {roll_no} not found!")
    
    def update_grade(self, roll_no, new_grade):
        if roll_no in self.students:
            self.students[roll_no].update_grade(new_grade)
            print(f"Grade updated for Roll No {roll_no}.")
        else:
            print(f"Student with Roll No {roll_no} not found!")
    
    def view_students(self):
        if self.students:
            print("Class List:")
            for student in self.students.values():
                print(student)
        else:
            print("No students in the class.")
            
def school_operation():
    school = School()
    
    def add_student_case():
        roll_no = int(input("Enter the Roll No: "))
        name = input("Enter the Name: ")
        grade = input("Enter the Grade: ")
        school.add_student(roll_no, name, grade)
        
    def update_grade_case():
        roll_no = int(input("Enter the Roll No: "))
        new_grade = input("Enter the New Grade: ")
        school.update_grade(roll_no, new_grade)

    def remove_student_case():
        roll_no = int(input("Enter Roll No to remove: "))
        school.remove_student(roll_no)

    def view_students_case():
        school.view_students()

    def exit_case():
        print("Exiting... Thank you for using the School Management System!")
        return False

    switch = {
        1: add_student_case,
        2: update_grade_case,
        3: remove_student_case,
        4: view_students_case,
        5: exit_case,
    }

    while True:
        print("\n--- School Management Menu ---")
        print("1. Add a Student")
        print("2. Update Student Grade")
        print("3. Remove a Student")
        print("4. View Class List")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice in switch:
                result = switch[choice]()
                if result is False:
                    break
            else:
                print("Invalid choice! Please try again.")
        except ValueError:
            print("Please enter a valid number.")

# Run the school operations
school_operation()
