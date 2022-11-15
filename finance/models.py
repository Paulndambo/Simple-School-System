from django.db import models
from students.models import Student
# Create your models here.
SEMESTER_CHOICES = (
    ("1", "Semester One"),
    ("2", "Semester Two"),
    ("3", "Semester Three"),
)

PAYMENT_METHODS = (
    ("mpesa", "M-pesa"),
    ("bank", "Bank"),
    ("cash", "Cash"),
)

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    invoice = models.DecimalField(max_digits=20, decimal_places=2)
    semester = models.CharField(max_length=255, choices=SEMESTER_CHOICES)
    balance = models.DecimalField(max_digits=20, decimal_places=2, null=True)

    def __str__(self):
        return self.student.name


class FeePayment(models.Model):
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHODS)
    date_paid = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)