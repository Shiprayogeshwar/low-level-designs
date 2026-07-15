from models import Student
from views import StudentView
from controllers import StudentController


if __name__ == "__main__":
    student = Student(1, "Shipra", 49)
    view = StudentView()
    controller = StudentController(student, view)

    controller.show_student()

    controller.update_marks(95)

    print("After updating marks")

    controller.show_student()
