class Student:
    def __init__(self, full_name, section, spanish, english, social_studies, science):
        self.full_name = full_name
        self.section = section
        self.spanish = float(spanish)
        self.english = float(english)
        self.social_studies = float(social_studies)
        self.science = float(science)
        self.average = self.calculate_average()

    def calculate_average(self):
        """Calculates the average grade of the student."""
        return (self.spanish + self.english + self.social_studies + self.science) / 4.0

    def to_dict(self):
        """Converts the Student object back to a dictionary for CSV export."""
        return {
            "full_name": self.full_name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "social_studies": self.social_studies,
            "science": self.science,
            "average": self.average
        }
