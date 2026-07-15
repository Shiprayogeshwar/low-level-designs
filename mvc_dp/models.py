class Student:
    def __init__(self, student_id, student_name, marks):
        self.id = student_id
        self.name = student_name
        self.marks = marks

    def update_marks(self, marks):
        self.marks = marks