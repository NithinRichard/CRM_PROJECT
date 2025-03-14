# from django.db import models

# from students.models import BaseClass

#  Create your models here.

# class PaymentSettleChoices(models.TextChoices):

#     ONE_TIME = "One Time","One Time"

#     INSTALLMENTS = "Installments","Installments"

    
# class InstallmentChoices(models.IntegerChoices):

#     TWO = 2,"2"

#     THREE = 3,"3"

#     FOUR = 4,"4"

#     FIVE = 5,"5"

#     SIX = 6,"6"


# class PaymentStructure(BaseClass):

#     student = models.OneToOneField("students.Students",on_delete=models.CASCADE)

#     one_time_or_installments = models.CharField(max_length=20,choices=PaymentSettleChoices.choices)

#     no_of_installments = models.IntegerField(choices=InstallmentChoices.choices,null=True,blank=True)

#     fee_to_be_paid = models.FloatField()

#     def __str__(self):

#         return f"{self.student.first_name} {self.student.batch.name} Payment Structure"
    
#     class Meta:

#         verbose_name = "Payment Structure"

#         verbose_name_plural = "Payment Structure"

from django.db import models

from students.models import BaseClass

class PaymentStatusChoice(models.TextChoices):

    PENDING = "Pending","Pending"

    SUCCESS = "Success","Success"

    FAILED = "Failed","Failed"


class Payment(BaseClass):

    student = models.OneToOneField("students.Students",on_delete=models.CASCADE)

    amount = models.FloatField()

    status = models.CharField(max_length=30,choices=PaymentStatusChoice.choices,default=PaymentStatusChoice.PENDING)

    paid_at = models.DateField(null=True,blank=True)

    
    def __str__(self):

        return f"{self.student.first_name} {self.student.batch.name}"
    
    class Meta:

        verbose_name = "Payments"

        verbose_name_plural = "Payments"

class Transactions(BaseClass):

    payment = models.ForeignKey("Payment",on_delete=models.CASCADE)

    rzp_order_id = models.SlugField()

    amount = models.FloatField()

    status = models.CharField(max_length=20,choices=PaymentStatusChoice.choices,default=PaymentStatusChoice.PENDING)

    transaction_at = models.DateTimeField(null=True,blank=True)

    rzp_payment_id = models.SlugField(null=True,blank=True)

    rzp_signature = models.TextField(null=True,blank=True)

    def __str__(self):

        return f"{self.payment.student.first_name} {self.payment.student.batch.name} {self.status}"
    
    class Meta:

        verbose_name = "Transactions"

        verbose_name_plural = "Transactions"

    




