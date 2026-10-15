import actions
import data

def display_menu():
    """Prints the main menu options."""
    print("\n" + "=" * 40)
    print("   STUDENT CONTROL SYSTEM - LYFTER")
    print("=" * 40)
    print("1. Add a new student")
    print("2. View all students")
    print("3. View Top 3 students")
    print("4. View overall average grade")
    print("5. Export student data to CSV")
    print("6. Import student data from CSV")
    print("7. Exit")
    print("=" * 40)


def run_menu():
    """Runs the main menu loop."""
    students = []

    while True:
        display_menu()
        option = input("Select an option (1-7): ").strip()

        if option == "1":
            actions.add_student(students)
        elif option == "2":
            actions.view_all_students(students)
        elif option == "3":
            actions.view_top_3_students(students)
        elif option == "4":
            actions.view_overall_average(students)
        elif option == "5":
            data.export_students_to_csv(students)
        elif option == "6":
            imported_data = data.import_students_from_csv()
            if imported_data:
                students = imported_data
        elif option == "7":
            print("\nExiting Student Control System. Goodbye!")
            break
        else:
            print("\n[!] Invalid option. Please select a number between 1 and 7.")
