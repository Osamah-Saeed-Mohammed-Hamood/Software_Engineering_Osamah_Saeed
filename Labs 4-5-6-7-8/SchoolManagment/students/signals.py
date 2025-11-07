from django.db.models.signals import post_save ,post_delete
from django.dispatch import receiver
from notifications.signals import notify
from .models import Student
from django.contrib.auth.models import User


@receiver (post_save,sender = Student)
def student_created_notification(sender,instance,created,**kwargs):
    admins = User.objects.filter(is_staff = True)
    if created:
        for admin in admins:
            notify.send(
                instance,
                recipient = admin,
                verb = "تم إضافة طالب جديد",
                description = f"تم إضافة  {instance.f_name} {instance.l_name}"
            )
    else:
        if instance._state.adding is False:
            for admin in admins:
                notify.send(
                    instance,
                    recipient = admin,
                    verb = "تم تعديل بيانات الطالب",
                    description = f"تم تعديل بيانات {instance.f_name} {instance.l_name}"
                )

@receiver (post_delete,sender = Student)
def student_deleted_notification(sender,instance,**kwargs):
    if instance:
        admin_user = User.objects.filter(is_staff = True)
        for admin in admin_user:
            notify.send(
                instance,
                recipient = admin,
                verb = "تم حذف الطالب ",
                description = f"تم حذف  {instance.f_name} {instance.l_name}"
            )

