import json

FILE_NAME = "students.json"


# Load students from file
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


# Save students to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Add student
def add_student(students):
    student_id = input("Enter student ID: ")
    
    for student in students:
        if student["id"] == student_id:
            print("Student already exists!")
            return

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    major = input("Enter major: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "major": major
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")


# Display students
def show_students(students):

    if len(students) == 0:
        print("No students found!")
        return

    print("\n--- Student List ---")

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Major: {student['major']}"
        )


# Search student
def search_student(students):

    keyword = input("Enter student ID: ")

    for student in students:
        if student["id"] == keyword:
            print("\nStudent Found:")
            print(student)
            return

    print("Student not found!")


# Update student
def update_student(students):

    student_id = input("Enter student ID to update: ")

    for student in students:

        if student["id"] == student_id:

            print("Leave blank if you don't want to change")

            name = input("New name: ")
            age = input("New age: ")
            major = input("New major: ")

            if name:
                student["name"] = name

            if age:
                student["age"] = int(age)

            if major:
                student["major"] = major

            save_students(students)

            print("Updated successfully!")
            return

    print("Student not found!")


# Delete student
def delete_student(students):

    student_id = input("Enter student ID to delete: ")

    for student in students:

        if student["id"] == student_id:

            students.remove(student)
            save_students(students)

            print("Deleted successfully!")
            return

    print("Student not found!")


# Main program
def main():

    students = load_students()

    while True:

        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            show_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


main()