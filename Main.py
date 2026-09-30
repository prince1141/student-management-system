students = {}


def add_student():
    roll = input("Enter roll number: ").strip()
    if roll in students:
        print("A student with this roll number already exists.")
        return
    name = input("Enter name: ").strip()
    course = input("Enter course: ").strip()
    students[roll] = {"name": name, "course": course}
    print("Student added.")


def view_students():
    if not students:
        print("No student records yet.")
        return
    print("\nRoll No | Name | Course")
    print("-" * 30)
    for roll, info in students.items():
        print(f"{roll} | {info['name']} | {info['course']}")


def search_student():
    roll = input("Enter roll number to search: ").strip()
    if roll in students:
        info = students[roll]
        print(f"Found: {roll} | {info['name']} | {info['course']}")
    else:
        print("Student not found.")


def delete_student():
    roll = input("Enter roll number to delete: ").strip()
    if roll in students:
        del students[roll]
        print("Student deleted.")
    else:
        print("Student not found.")


def main():
    while True:
        print("\n=== Student Management System ===")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Delete student")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
