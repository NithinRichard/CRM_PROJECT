import uuid

from .models import Students

import string

import random

from django.conf import settings

from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string



def get_admission_number():

    pattern = str(uuid.uuid4().int)[:7]

    admission_number = f"LM-E{pattern}"

    if not Students.objects.filter(adm_number=admission_number).exists():

        return admission_number
    

# string.ascii_letters - "a,b,c,A,Z..."

def get_password():

    password ="".join(random.choices(string.ascii_letters+string.digits,k=8))

    return password

#email sending

def send_email(subject,recepients,template,context):

    email_obj = EmailMultiAlternatives(subject,from_email=settings.EMAIL_HOST_USER,to=recepients)

    content = render_to_string(template_name=template,context=context)

    email_obj.attach_alternative(content,'text/html')

    email_obj.send()

    



