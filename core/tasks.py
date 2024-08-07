from celery import shared_task
from home.models import Student

@shared_task
def delete_student_objects():
    # Find and delete the most recently added student object
    latest_student = Student.objects.order_by('-id').first()
    if latest_student:
        latest_student.delete()
        print(f"Deleted student: {latest_student.name} {latest_student.surname}")
    else:
        print("No students to delete.")