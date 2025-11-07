from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from notifications.models import Notification
from students.models import Student
from django.http import HttpResponse

# Create your views here.

@login_required(login_url='user:login')
def index(request):
    notifications = Notification.objects.filter(recipient_id = request.user.id)

    notification_count = notifications.filter(unread = True).count()

    all_notification_count = notifications.count()

    context = {
        "notificationCount" : notification_count,
        "all_notification_count" : all_notification_count,
        "notification" : notifications if all_notification_count > 0 else "no notifications found"
    }
    return render (request,'navbar.html',context)

@login_required(login_url='user:login')
def read(request,pk):
    try:
        notification = Notification.objects.get(id = pk)
        notification.unread = False
        notification.save()
    except Notification.DoesNotExist:
        return redirect('notifications:error_page')
    return redirect('students:all_students')

def delete(request,pk):
    notification = Notification.objects.get(id=pk).delete()
    return redirect('students:home')  