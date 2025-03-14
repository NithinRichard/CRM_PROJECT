from django.db import models
from students.models import BaseClass, DistrictChoices

class QualificationChoices(models.TextChoices):
    UG = "UG", "Undergraduate"
    PG = "PG", "Postgraduate"
    DIPLOMA = "DIPLOMA", "Diploma"

class Trainers(BaseClass):
    profile = models.OneToOneField(
        "authentication.Profile",
        on_delete=models.CASCADE,
        related_name="trainer"
    )
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    employee_id = models.CharField(max_length=10, unique=True)
    photo = models.ImageField(upload_to='trainers/photos/%Y/%m/%d/')
    email = models.EmailField(unique=True)
    contact_num = models.CharField(max_length=12)
    house_name = models.CharField(max_length=25)
    post_office = models.CharField(max_length=25)
    district = models.CharField(max_length=20, choices=DistrictChoices.choices)
    pincode = models.CharField(max_length=6)
    qualification = models.CharField(max_length=10, choices=QualificationChoices.choices)
    stream = models.CharField(max_length=25)
    id_proof = models.FileField(upload_to='trainers/idproof/%Y/%m/%d/')
    course = models.ForeignKey(
        "courses.Courses",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="trainers"
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Trainer'
        verbose_name_plural = 'Trainers'