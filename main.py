# Display the main menu
def show_menu():
    print("===== Student Management System =====")
    print("1. Add Student\n2. Show Student\n3. Calculate Average\n4. Search Student\n5. Exit ")


# Store all student records
students = []


# Add a new student with their name and grade
def add_student():

    name = input("Enter student name: ")
    grade = float(input("Enter grade: "))

    student = {
        "name": name,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully")


# Display all stored students and their grades
def show_student():

    if not students:
        print("No students added")
        return

    for student in students:
        print("Student name: ", student["name"])
        print("Grade:", student["grade"])
        print("---------------------------")


# Calculate the average grade of all students
def calculate_average():

    if not students:
        print("No students added")
        return

    grades = 0

    for student_grades in students:
        grades += student_grades["grade"]

    avg = grades / len(students)
    print(f"Average Grade: {avg:.2f}")


# Search for a student by name
def search_student():

    if not students:
        print("No students added")
        return

    search_name = input("Enter student name: ")

    found = False

    for search in students:
        if search["name"] == search_name:
            print("Student name:", search["name"])
            print("Grade:", search["grade"])
            found = True

    if not found:
        print("student not found")


while True:
    show_menu()

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        show_student()

    elif choice == 3:
        calculate_average()

    elif choice == 4:
        search_student()

    elif choice == 5:
        break

    else:
        print("Invalid choice")