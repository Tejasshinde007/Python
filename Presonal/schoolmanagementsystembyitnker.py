import tkinter as tk
from tkinter import messagebox

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
            return f"Student with Roll No {roll_no} already exists!"
        else:
            self.students[roll_no] = Student(roll_no, name, grade)
            return f"Student {name} (Roll No: {roll_no}) has been added successfully."

    def remove_student(self, roll_no):
        if roll_no in self.students:
            removed_student = self.students.pop(roll_no)
            return f"Student {removed_student.name} (Roll No: {roll_no}) removed successfully."
        else:
            return f"Student with Roll No {roll_no} not found!"

    def update_grade(self, roll_no, new_grade):
        if roll_no in self.students:
            self.students[roll_no].update_grade(new_grade)
            return f"Grade updated for Roll No {roll_no}."
        else:
            return f"Student with Roll No {roll_no} not found!"

    def view_students(self):
        if self.students:
            return "\n".join(str(student) for student in self.students.values())
        else:
            return "No students in the class."


class SchoolApp:
    def __init__(self, root):
        self.school = School()
        self.root = root
        self.root.title("School Management System")

        # Title Label
        self.title_label = tk.Label(root, text="School Management System", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(root, text="Add Student", command=self.add_student_ui, width=20)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Grade", command=self.update_grade_ui, width=20)
        self.update_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remove Student", command=self.remove_student_ui, width=20)
        self.remove_button.pack(pady=5)

        self.view_button = tk.Button(root, text="View Students", command=self.view_students_ui, width=20)
        self.view_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit, width=20)
        self.exit_button.pack(pady=5)

    def add_student_ui(self):
        self.popup_window("Add Student", self.add_student)

    def add_student(self, roll_no, name, grade):
        message = self.school.add_student(roll_no, name, grade)
        messagebox.showinfo("Add Student", message)

    def update_grade_ui(self):
        self.popup_window("Update Grade", self.update_grade, update=True)

    def update_grade(self, roll_no, grade):
        message = self.school.update_grade(roll_no, grade)
        messagebox.showinfo("Update Grade", message)

    def remove_student_ui(self):
        self.popup_window("Remove Student", self.remove_student, remove=True)

    def remove_student(self, roll_no):
        message = self.school.remove_student(roll_no)
        messagebox.showinfo("Remove Student", message)

    def view_students_ui(self):
        students = self.school.view_students()
        messagebox.showinfo("Class List", students)

    def popup_window(self, title, action, update=False, remove=False):
        popup = tk.Toplevel(self.root)
        popup.title(title)

        tk.Label(popup, text="Roll No:").grid(row=0, column=0, padx=10, pady=5)
        roll_no_entry = tk.Entry(popup)
        roll_no_entry.grid(row=0, column=1, padx=10, pady=5)

        if not remove:
            if update:
                tk.Label(popup, text="New Grade:").grid(row=1, column=0, padx=10, pady=5)
                input_entry = tk.Entry(popup)
                input_entry.grid(row=1, column=1, padx=10, pady=5)
            else:
                tk.Label(popup, text="Name:").grid(row=1, column=0, padx=10, pady=5)
                name_entry = tk.Entry(popup)
                name_entry.grid(row=1, column=1, padx=10, pady=5)

                tk.Label(popup, text="Grade:").grid(row=2, column=0, padx=10, pady=5)
                input_entry = tk.Entry(popup)
                input_entry.grid(row=2, column=1, padx=10, pady=5)

        def on_submit():
            roll_no = roll_no_entry.get()
            if not roll_no.isdigit():
                messagebox.showerror("Error", "Roll No must be a number!")
                return

            roll_no = int(roll_no)
            if remove:
                action(roll_no)
            elif update:
                grade = input_entry.get()
                action(roll_no, grade)
            else:
                name = name_entry.get()
                grade = input_entry.get()
                action(roll_no, name, grade)

            popup.destroy()

        submit_button = tk.Button(popup, text="Submit", command=on_submit)
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolApp(root)
    root.mainloop()
