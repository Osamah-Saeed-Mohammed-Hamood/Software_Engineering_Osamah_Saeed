from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.timezone import now
from django.core.mail import EmailMessage

# Create your views here.

def send_welcome_email (username, recipient_email):
    subject = "Welcome to Our Platform!"
    from_email = 'engosamahsaeed@gmail.com'
    recipient_list = [recipient_email]

    context = {
        'username':username,
        'year':now().year,
    }

    html_message = render_to_string('welcome.html',context)

    try:
        email_message = EmailMessage(subject, html_message ,from_email, recipient_list)
        email_message.content_subtype = 'html'
        sent = email_message.send()
        return sent > 0
    except Exception as e:
        print(f"Error sending email {e}")
        return False
    



