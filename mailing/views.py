from django.shortcuts import render,redirect
from django.core.mail import send_mail as mymail
from django.conf import settings
from pathlib import Path
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# inform about facilitator registration
def RegistrationSuccessAdminEmail(name,catlist):
    subject = 'About collaboration'
    message = name+""" Wants to collaborate With Us and Showing Intrest in """+catlist
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['vijaygwala97@gmail.com',]
    mymail( subject, message, email_from, recipient_list ,fail_silently=False)
    





# the function for sending an email
def send_email(subject, text_content, html_content=None, sender=None, recipient=None, image_path=None, image_name=None):
    email = EmailMultiAlternatives(subject=subject, body=text_content, from_email=sender, to=recipient if isinstance(recipient, list) else [recipient])

    if all([html_content,image_path,image_name]):
        email.attach_alternative(html_content, "text/html")
        email.content_subtype = 'html'  # set the primary content to be text/html
        email.mixed_subtype = 'related' # it is an important part that ensures embedding of an image 

        with open(image_path, mode='rb') as f:
            image = MIMEImage(f.read())
            
            image.add_header('Content-ID', f"<{image_name}>")
            email.attach(image)

    email.send()
def registration(request):
    return render(request,'html/shortlisted.html')

def successOnRegistration(to,template):
    recipient = [to]
    sender =settings.EMAIL_HOST_USER # 
    image_path = Path.cwd() / 'static' / 'email'/template
    image_name = Path(image_path).name
    

    subject = "Thankyou for Becoming a ChangeMaker"
    context={
        'image_name':image_name
     }
    text_message = f"Email with a nice embedded image {image_name}."
   
    html_message=render_to_string('html/before_payment.html',context)
#     
    send_email(subject="TMHM PVT LTD", text_content=text_message, html_content=html_message, sender=sender, recipient=recipient, image_path=image_path, image_name=image_name)


def successOnShortlisted(recipient_list,template):
    
    recipient = recipient_list
    sender =settings.EMAIL_HOST_USER # 
    image_path = Path.cwd() / 'static' / 'email'/template
    image_name = Path(image_path).name
    

    subject = "Thankyou for Becoming a ChangeMaker"
    context={
        'image_name':image_name
     }
    text_message = f"Email with a nice embedded image {image_name}."
   
    html_message=render_to_string('html/shortlisted.html',context)
#     
    send_email(subject="TMHM PVT LTD", text_content=text_message, html_content=html_message, sender=sender, recipient=recipient, image_path=image_path, image_name=image_name)


