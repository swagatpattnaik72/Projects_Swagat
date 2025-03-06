# Initialising the dictionary

student_grades = {}

def add_student (name, grade):
    student_grades [name] = grade
    print (f"Added {name} with a {grade}")
def update_student (name, grade):
    if name in student_grades:
        student_grades[name] = grade

        print (f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found!")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found!")
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")

    else:
        print ("No students found/added")
display_all_students()

def main():
    while True:
        print('\n Student Grades Management System')
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice = int(input("Enter your choice = "))
        if choice == 1:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            add_student(name, grade)
        elif choice == 2:
            name = input("Enter student name = ")
            grade = int(input("Enter student grade = "))
            update_student(name, grade)
            
        elif choice == 3:
            name = input("Enter student name = ")
            delete_student(name)

        elif choice == 4:
            




