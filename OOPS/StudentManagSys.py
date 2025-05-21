# Student management system in Python

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"{self.student_id}: {self.name}, Age {self.age}, Grade {self.grade}"

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def remove_student(self, student_id):
        self.students.pop(student_id, None)

    def display_students(self):
        if not self.students:
            print("No students.")
        else:
            for s in self.students.values():
                print(s)

    def find_student(self, student_id):
        return self.students.get(student_id)

if __name__ == "__main__":
    sms = StudentManagementSystem()
    while True:
        print("\n1. Add\n2. Remove\n3. Display\n4. Find\n5. Exit")
        c = input("Choice: ")
        if c == '1':
            sid = input("ID: ")
            name = input("Name: ")
            age = input("Age: ")
            grade = input("Grade: ")
            sms.add_student(Student(sid, name, age, grade))
        elif c == '2':
            sms.remove_student(input("ID to remove: "))
        elif c == '3':
            sms.display_students()
        elif c == '4':
            s = sms.find_student(input("ID to find: "))
            print(s if s else "Not found.")
        elif c == '5':
            break
        else:
            print("Invalid.")

# Code by Harshit