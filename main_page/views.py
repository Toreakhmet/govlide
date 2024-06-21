from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

def send_email(request):
    if request.method == 'POST':
        sender_name = request.POST.get('name')
        phone_number = request.POST.get('number')
        email = request.POST.get('email')

        subject = 'New Message from Your Website'
        message = f"""
        You have received a new message from {sender_name}.
        
        Phone Number: {phone_number}
        
        Email: {email}
        """
        
        html_message = f"""
        <html>
            <body>
                <h2 style="background-color:black;">New Message from Your Website</h2>
                <p><strong>Name:</strong> {sender_name}</p>
                <p><strong>Phone Number:</strong> {phone_number}</p>
                <p><strong>Email:</strong> {email}</p>
            </body>
        </html>
        """
        
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['xgvcdvvu@bk.ru']
        
        send_mail(subject, message, email_from, recipient_list, html_message=html_message)
        return redirect('home')
    return render(request, 'send_email.html')
