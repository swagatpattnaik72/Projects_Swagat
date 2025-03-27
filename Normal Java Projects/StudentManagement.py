# Initialising the dictionary
student_grades = {}

def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a grade of {grade}.")1

def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s grade has been updated to {grade}.")
    else:
        print(f"{name} is not found!")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted.")
    else:
        print(f"{name} is not found!")

def display_all_students():
    if student_grades:
        print("\nStudent List:")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found/added.")

def main():
    while True:
        print('\n--- Student Grades Management System ---')
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            name = input("Enter student name: ").strip()
            try:
                grade = int(input("Enter student grade: "))
                add_student(name, grade)
            except ValueError:
                print("Invalid grade. Please enter a number.")

        elif choice == 2:
            name = input("Enter student name: ").strip()
            try:
                grade = int(input("Enter updated grade: "))
                update_student(name, grade)
            except ValueError:
                print("Invalid grade. Please enter a number.")

        elif choice == 3:
            name = input("Enter student name to delete: ").strip()
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing the Program....")
            break

        else:
            print("Invalid Choice! Please select between 1-5.")

if __name__ == "__main__":
    main()

            




