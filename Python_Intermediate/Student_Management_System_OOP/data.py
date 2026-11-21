import csv
import os
from student import Student

FILE_PATH = "students_data.csv"

def export_students_to_csv(students_list):
    """Converts Student objects to dictionaries and exports them to CSV."""
    if not students_list:
        print("\n[!] No student data available to export.")
        return

    headers = ["full_name", "section", "spanish", "english", "social_studies", "science", "average"]
    
    # Convertimos cada objeto Student a un diccionario usando student.to_dict()
    export_data = [student.to_dict() for student in students_list]

    try:
        with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(export_data)
        print(f"\n[✓] Data successfully exported to {FILE_PATH}!")
    except Exception as e:
        print(f"\n[X] Error exporting data: {e}")


def import_students_from_csv():
    """Reads CSV rows (dictionaries) and converts them into Student objects."""
    if not os.path.exists(FILE_PATH):
        print(f"\n[!] File '{FILE_PATH}' does not exist. Please export data first.")
        return []

    students_list = []
    try:
        with open(FILE_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convertimos la fila (diccionario) en una instancia de Student
                student_obj = Student(
                    full_name=row["full_name"],
                    section=row["section"],
                    spanish=row["spanish"],
                    english=row["english"],
                    social_studies=row["social_studies"],
                    science=row["science"]
                )
                students_list.append(student_obj)
        print(f"\n[✓] Data successfully imported from {FILE_PATH} as Objects!")
        return students_list
    except Exception as e:
        print(f"\n[X] Error importing data: {e}")
        return []
