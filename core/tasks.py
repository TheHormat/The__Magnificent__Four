from celery import shared_task
from home.models import Student


@shared_task
def delete_student_objects():
    if latest_student := Student.objects.order_by("-id").first():
        latest_student.delete()
        print(f"Deleted student: {latest_student.name} {latest_student.surname}")
    else:
        print("No students to delete.")
