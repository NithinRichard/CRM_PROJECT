import uuid

from .models import Students

import string

import random

def get_admission_number():

    pattern = str(uuid.uuid4().int)[:7]

    admission_number = f"LM-{pattern}"

    if not Students.objects.filter(adm_number=admission_number).exists():

        return admission_number
    

# string.ascii_letters - "a,b,c,A,Z..."

def get_password():

    password ="".join(random.choices(string.ascii_letters+string.digits,k=8))

    return password


