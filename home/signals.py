from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Student
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@receiver(post_save, sender=Student)
def student_saved(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "students",
        {
            "type": "student_message",
            "message": f"Student {instance.name} {instance.surname} has been added.",
        },
    )


@receiver(post_delete, sender=Student)
def student_deleted(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "students",
        {
            "type": "student_message",
            "message": f"Student {instance.name} {instance.surname} has been deleted.",
        },
    )
