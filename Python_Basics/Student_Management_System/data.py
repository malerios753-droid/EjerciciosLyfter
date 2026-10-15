import csv
import os

FILE_PATH = "students_data.csv"

def export_students_to_csv(students_list):
    """Exports the list of student dictionaries to a CSV file."""
    if not students_list:
        print("\n[!] No student data available to export.")
        return

    headers = ["full_name", "section", "spanish", "english", "social_studies", "science", "average"]
    
    try:
        with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(students_list)
        print(f"\n[✓] Data successfully exported to {FILE_PATH}!")
    except Exception as e:
        print(f"\n[X] Error exporting data: {e}")


def import_students_from_csv():
    """Imports student data from a CSV file into a list of dictionaries."""
    if not os.path.exists(FILE_PATH):
        print(f"\n[!] File '{FILE_PATH}' does not exist. Please export data first.")
        return []

    students_list = []
    try:
        with open(FILE_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students_list.append({
                    "full_name": row["full_name"],
                    "section": row["section"],
                    "spanish": float(row["spanish"]),
                    "english": float(row["english"]),
                    "social_studies": float(row["social_studies"]),
                    "science": float(row["science"]),
                    "average": float(row["average"])
                })
        print(f"\n[✓] Data successfully imported from {FILE_PATH}!")
        return students_list
    except Exception as e:
        print(f"\n[X] Error importing data: {e}")
        return []
