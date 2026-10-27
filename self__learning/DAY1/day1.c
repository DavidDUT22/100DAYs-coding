    #include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STUDENTS 100
#define NAME_LEN 50
#define FILE_NAME "students.dat"

typedef struct {
    int roll;
    char name[NAME_LEN];
    float marks;
} Student;

Student students[MAX_STUDENTS];
int studentCount = 0;

/* Clear leftover input in the buffer (fixes scanf + getchar issues) */
void clearInputBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

/* Load students from file at program start */
void loadFromFile() {
    FILE *fp = fopen(FILE_NAME, "rb");
    if (fp == NULL) {
        return; /* no file yet, that's fine */
    }
    studentCount = fread(students, sizeof(Student), MAX_STUDENTS, fp);
    fclose(fp);
}

/* Save students to file */
void saveToFile() {
    FILE *fp = fopen(FILE_NAME, "wb");
    if (fp == NULL) {
        printf("Error: could not save data to file.\n");
        return;
    }
    fwrite(students, sizeof(Student), studentCount, fp);
    fclose(fp);
}

/* Find index of a student by roll number, -1 if not found */
int findStudentIndex(int roll) {
    for (int i = 0; i < studentCount; i++) {
        if (students[i].roll == roll) {
            return i;
        }
    }
    return -1;
}

void addStudent() {
    if (studentCount >= MAX_STUDENTS) {
        printf("Student list is full. Cannot add more.\n");
        return;
    }

    Student s;

    printf("Enter roll number: ");
    if (scanf("%d", &s.roll) != 1) {
        printf("Invalid input for roll number.\n");
        clearInputBuffer();
        return;
    }
    clearInputBuffer();

    if (findStudentIndex(s.roll) != -1) {
        printf("A student with roll number %d already exists.\n", s.roll);
        return;
    }

    printf("Enter name: ");
    fgets(s.name, NAME_LEN, stdin);
    s.name[strcspn(s.name, "\n")] = '\0'; /* remove trailing newline */

    printf("Enter marks: ");
    if (scanf("%f", &s.marks) != 1) {
        printf("Invalid input for marks.\n");
        clearInputBuffer();
        return;
    }
    clearInputBuffer();

    students[studentCount] = s;
    studentCount++;
    saveToFile();
    printf("Student added successfully.\n");
}

void displayAllStudents() {
    if (studentCount == 0) {
        printf("No students to display.\n");
        return;
    }

    printf("\n%-10s %-30s %-10s\n", "Roll No", "Name", "Marks");
    printf("--------------------------------------------------\n");
    for (int i = 0; i < studentCount; i++) {
        printf("%-10d %-30s %-10.2f\n",
               students[i].roll, students[i].name, students[i].marks);
    }
}

void searchStudent() {
    int roll;
    printf("Enter roll number to search: ");
    if (scanf("%d", &roll) != 1) {
        printf("Invalid input.\n");
        clearInputBuffer();
        return;
    }
    clearInputBuffer();

    int idx = findStudentIndex(roll);
    if (idx == -1) {
        printf("No student found with roll number %d.\n", roll);
        return;
    }

    printf("\nRoll No: %d\nName: %s\nMarks: %.2f\n",
           students[idx].roll, students[idx].name, students[idx].marks);
}

void updateStudent() {
    int roll;
    printf("Enter roll number to update: ");
    if (scanf("%d", &roll) != 1) {
        printf("Invalid input.\n");
        clearInputBuffer();
        return;
    }
    clearInputBuffer();

    int idx = findStudentIndex(roll);
    if (idx == -1) {
        printf("No student found with roll number %d.\n", roll);
        return;
    }

    printf("Enter new name: ");
    fgets(students[idx].name, NAME_LEN, stdin);
    students[idx].name[strcspn(students[idx].name, "\n")] = '\0';

    printf("Enter new marks: ");
    if (scanf("%f", &students[idx].marks) != 1) {
        printf("Invalid input for marks.\n");
        clearInputBuffer();
        return;
    }
    clearInputBuffer();

    saveToFile();
    printf("Student updated successfully.\n");
}

void deleteStudent() {
    int roll;
    printf("Enter roll number to delete: ");
    if (scanf("%d", &roll) != 1) {
        printf("Invalid input.\n");
        clearInputBuffer();
        return;
    }
    clearInputBuffer();

    int idx = findStudentIndex(roll);
    if (idx == -1) {
        printf("No student found with roll number %d.\n", roll);
        return;
    }

    for (int i = idx; i < studentCount - 1; i++) {
        students[i] = students[i + 1];
    }
    studentCount--;
    saveToFile();
    printf("Student deleted successfully.\n");
}

void printMenu() {
    printf("\n===== Student Management System =====\n");
    printf("1. Add Student\n");
    printf("2. Display All Students\n");
    printf("3. Search Student by Roll Number\n");
    printf("4. Update Student\n");
    printf("5. Delete Student\n");
    printf("6. Exit\n");
    printf("Enter your choice: ");
}

int main() {
    loadFromFile();

    int choice;
    do {
        printMenu();
        if (scanf("%d", &choice) != 1) {
            printf("Invalid input. Please enter a number.\n");
            clearInputBuffer();
            continue;
        }
        clearInputBuffer();

        switch (choice) {
            case 1: addStudent(); break;
            case 2: displayAllStudents(); break;
            case 3: searchStudent(); break;
            case 4: updateStudent(); break;
            case 5: deleteStudent(); break;
            case 6: printf("Exiting. Goodbye!\n"); break;
            default: printf("Invalid choice. Try again.\n");
        }
    } while (choice != 6);

    return 0;
} 