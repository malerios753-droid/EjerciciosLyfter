def get_valid_grade(subject_name):
    """Prompts for a grade until a valid number between 0 and 100 is entered."""
    while True:
        try:
            grade = float(input(f"Enter grade for {subject_name} (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("[!] Grade must be between 0 and 100. Try again.")
        except ValueError:
            print("[!] Invalid input. Please enter a valid numeric grade.")


def add_student(students_list):
    """Collects student information and appends it to the students list."""
    print("\n--- Add New Student ---")
    full_name = input("Enter full name: ").strip()
    section = input("Enter section (e.g., 11B): ").strip()

    spanish = get_valid_grade("Spanish")
    english = get_valid_grade("English")
    social_studies = get_valid_grade("Social Studies")
    science = get_valid_grade("Science")

    average = (spanish + english + social_studies + science) / 4.0

    student = {
        "full_name": full_name,
        "section": section,
        "spanish": spanish,
        "english": english,
        "social_studies": social_studies,
        "science": science,
        "average": average
    }

    students_list.append(student)
    print(f"\n[✓] Student '{full_name}' added successfully!")


def view_all_students(students_list):
    """Displays information for all registered students."""
    if not students_list:
        print("\n[!] No students registered yet.")
        return

    print("\n================ All Students ================")
    for index, student in enumerate(students_list, start=1):
        print(f"{index}. Name: {student['full_name']} | Section: {student['section']}")
        print(f"   Grades -> Spanish: {student['spanish']} | English: {student['english']} | Social Studies: {student['social_studies']} | Science: {student['science']}")
        print(f"   Average Grade: {student['average']:.2f}")
        print("-" * 46)


def view_top_3_students(students_list):
    """Displays the top 3 students with the highest average grades."""
    if not students_list:
        print("\n[!] No students registered yet.")
        return

    # Sort students by average grade in descending order
    sorted_students = sorted(students_list, key=lambda s: s['average'], reverse=True)
    top_3 = sorted_students[:3]

    print("\n================ Top 3 Students ================")
    for rank, student in enumerate(top_3, start=1):
        print(f"Rank {rank}: {student['full_name']} ({student['section']}) - Average: {student['average']:.2f}")


def view_overall_average(students_list):
    """Calculates and displays the overall average grade across all students."""
    if not students_list:
        print("\n[!] No students registered yet.")
        return

    total_sum = sum(student['average'] for student in students_list)
    overall_avg = total_sum / len(students_list)

    print(f"\n[i] Overall average grade across all {len(students_list)} student(s): {overall_avg:.2f}")
