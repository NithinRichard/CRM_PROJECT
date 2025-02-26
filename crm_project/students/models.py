from django.db import models

from django.utils import timezone

import uuid

# Create your models here.

class BaseClass(models.Model):

    uuid = models.SlugField(unique=True,default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True



class CourseChoices(models.TextChoices):

    #variable - databasevalue , representation

    

    PY_DJANGO = "PY-DJANGO","PY-DJANGO"

    MEARN = "MEARN","MEARN"

    DATA_SCIENCE = "DATA SCIENCE","DATA SCIENCE"

    SOFTWARE_TESTING = "SOFTWARE TESTING","SOFTWARE TESTING"

class DistrictChoices(models.TextChoices):

    THIRUVANANTHAPURAM = "Thiruvananthapuram", "Thiruvananthapuram"

    KOLLAM = "Kollam","Kollam"

    ALAPPUZHA = "Alappuzha","Alappuzha"

    PATHANAMTHITTA = "Pathanamthitta","Pathanamthitta"

    KOTTAYAM = "Kottayam","Kottayam"

    ERNAKULAM = "Ernakulam","Ernakulam"

    THRISSUR = "Thrissur","Thrissur"

    WAYANAD = "Wayanad","Wayanad"

    PALAKKAD = "Palakkad","Palakkad"

    KOZHIKODE = "Kozhikode","Kozhikode"

    MALAPPURAM = "Malappuram","Malappuram"

    KASARGOD = "Kasargod","Kasargod"

    IDUKKI = "Idukki","Idukki"

    KANNUR = "Kannur","Kannur"


class TrainerChoices(models.TextChoices):

    JOHN_DOE = "John Doe","John Doe"
    
    JAMES = "James","James"

    PETER = "Peter","Peter"

    ALEX = "Alex","Alex"

class BatchChoices(models.TextChoices):

    PY_NOV_2024 = "PY-NOV-2024","PY-NOV-2024"

    PY_JAN_2025 = "PY-JAN-2025","PY-JAN-2025"

    DS_JAN_2025 = "DS-JAN-2025","DS-JAN-2025"

    ST_JAN_2025 = "ST-JAN-2025","ST-JAN-2025"

    MEARN_NOV_2024 = "MEARN-NOV-2024","MEARN-NOV-2024"

    MEARN_JAN_2025 = "MEARN-NOV-2025","MEARN-NOV-2025"












class Students(BaseClass):

    # PERSONAL DETAILS FIELD

    profile = models.OneToOneField("authentication.PROFILE",on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    photo = models.ImageField(upload_to="students")

    email = models.EmailField(unique=True)

    contact_num = models.CharField(max_length=50)

    house_name = models.CharField(max_length=100)

    post_office = models.CharField(max_length=100)

    district = models.CharField(max_length=100,choices=DistrictChoices.choices)

    pincode = models.CharField(max_length=50)

    adm_number = models.CharField(max_length=50)

    

    #COURSE DETAILS FIELD

    # course = models.CharField(max_length=50,choices=CourseChoices.choices)

    course = models.ForeignKey("courses.Courses",null=True,on_delete=models.SET_NULL)
    
    # batch = models.CharField(max_length=50,choices=BatchChoices.choices)

    batch = models.ForeignKey("batches.Batches",null=True,on_delete=models.SET_NULL)



    # batch_date = models.DateField()

    join_date = models.DateField(auto_now_add=True)

    # trainer_name = models.CharField(max_length=50,choices=TrainerChoices.choices)

    trainer = models.ForeignKey("trainers.Trainers",null=True,on_delete=models.SET_NULL)


    def __str__(self):
        
        return f'{self.first_name} {self.last_name} {self.batch}'
    
    
    

    class Meta :

        verbose_name = "Students"

        verbose_name_plural = "Students"

        ordering = ["id"]




    

    

    

    

    


