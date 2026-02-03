def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")

    with open("students.txt", "a") as file:
        file.write(f"{roll},{name},{course}\n")

    print("Student added successfully!")


def view_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()
            if not students:
                print("No records found.")
            else:
                print("\nRoll\tName\tCourse")
                print("-" * 30)
                for student in students:
                    roll, name, course = student.strip().split(",")
                    print(f"{roll}\t{name}\t{course}")
    except FileNotFoundError:
        print("No records found.")


def search_student():
    roll_no = input("Enter roll number to search: ")
    found = False

    with open("students.txt", "r") as file:
        for student in file:
            roll, name, course = student.strip().split(",")
            if roll == roll_no:
                print(f"Student Found → Name: {name}, Course: {course}")
                found = True
                break

    if not found:
        print("Student not found.")


def delete_student():
    roll_no = input("Enter roll number to delete: ")
    students = []

    with open("students.txt", "r") as file:
        students = file.readlines()

    with open("students.txt", "w") as file:
        for student in students:
            roll, name, course = student.strip().split(",")
            if roll != roll_no:
                file.write(student)

    print("Student record deleted successfully!")


def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Try again.")


main()
