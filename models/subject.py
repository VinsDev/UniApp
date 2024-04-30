import random

class Subject:
    def __init__(self, ID):
        self.ID = ID
        self.mark = self.generate_mark()
        self.grade = self.determine_grade()

    def generate_mark(self):
        return random.randint(25, 100)

    def determine_grade(self):
        if self.mark >= 80:
            return "A"
        elif self.mark >= 70:
            return "B"
        elif self.mark >= 60:
            return "C"
        elif self.mark >= 50:
            return "D"
        else:
            return "F"
