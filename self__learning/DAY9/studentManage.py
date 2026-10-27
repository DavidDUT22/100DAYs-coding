students = []

def add_student():
    name = input("Enter student name: ")

    try:
        grade = float(input("Enter grade: "))
    except ValueError:
        print("Invalid grade!\n")
        return

    student = {
        "name": name,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if len(students) == 0:
        print("No students found.\n")
        return

    print("\nStudent List")

    for i, student in enumerate(students, start=1):
        print(f"{i}. {student['name']} - {student['grade']}")

    print()


def search_student():
    name = input("Enter student name: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print(f"\nName : {student['name']}")
            print(f"Grade: {student['grade']}\n")
            return

    print("Student not found.\n")


def update_grade():
    name = input("Enter student name: ")

    for student in students:
        if student["name"].lower() == name.lower():
            try:
                student["grade"] = float(input("Enter new grade: "))
                print("Grade updated.\n")
            except ValueError:
                print("Invalid grade.\n")
            return

    print("Student not found.\n")


def delete_student():
    name = input("Enter student name: ")

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student deleted.\n")
            return

    print("Student not found.\n")


def show_statistics():
    if len(students) == 0:
        print("No students available.\n")
        return

    total = 0
    highest = students[0]
    lowest = students[0]

    for student in students:
        total += student["grade"]

        if student["grade"] > highest["grade"]:
            highest = student

        if student["grade"] < lowest["grade"]:
            lowest = student

    average = total / len(students)

    print(f"Average Grade : {average:.2f}")
    print(f"Highest Grade : {highest['name']} ({highest['grade']})")
    print(f"Lowest Grade  : {lowest['name']} ({lowest['grade']})")
    print()


while True:
    print("===== Student Grade Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Grade")
    print("5. Delete Student")
    print("6. Show Statistics")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_grade()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        show_statistics()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.\n")