# students/context_processors.py
from notifications.models import Notification

def notifications_processor(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
        notification_count = notifications.filter(unread=True).count()
        all_notification_count = notifications.count()
        return {
            'notification': notifications,
            'notificationCount': notification_count,
            'all_notification_count': all_notification_count,
        }
    return {}
