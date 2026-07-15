class StudentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_marks(self, marks):
        self.model.update_marks(marks)

    def show_student(self):
        self.view.display(self.model)