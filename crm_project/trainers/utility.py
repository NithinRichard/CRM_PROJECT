from .models import Trainers

import string

import random

import uuid

def get_employee_id():

    pattern = str(uuid.uuid4().int)[:7]

    employee_num = f"LM-E{pattern}"

    if not Trainers.objects.filter(employee_id=employee_num).exists():

        return employee_num
    
# string.ascii_letters - "a,b,c,A,Z..."

def get_password():

    password ="".join(random.choices(string.ascii_letters+string.digits,k=8))

    return password