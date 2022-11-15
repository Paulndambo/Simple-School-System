from django.db import models
from django.contrib.auth.models import User
from core.models import Result

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    reg_number = models.CharField(max_length=255)
    birth_date = models.DateField()
    admission_date = models.DateField()
    current_year = models.CharField(max_length=255)
    class_teacher = models.ForeignKey(to="teachers.Teacher", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    @property
    def bit_111(self):
        result = Result.objects.filter(student_id=self.id, unit__unit_code='BIT 111').first()
        if result is not None:
            return result.total
        return 0

    @property
    def bit_113(self):
        result = Result.objects.filter(student_id=self.id, unit__unit_code='BIT 113').first()
        if result is not None:
            return result.total
        return 0

    @property
    def bit_121(self):
        result = Result.objects.filter(student_id=self.id, unit__unit_code='BIT 121').first()
        if result is not None:
            return result.total
        return 0

    @property
    def bit_123(self):
        result = Result.objects.filter(
            student_id=self.id, unit__unit_code='BIT 123').first()
        if result is not None:
            return result.total
        return 0

    @property
    def bit_141(self):
        result = Result.objects.filter(
            student_id=self.id, unit__unit_code='BIT 141').first()
        if result is not None:
            return result.total
        return 0

    @property
    def bit_145(self):
        result = Result.objects.filter(
            student_id=self.id, unit__unit_code='BIT 145').first()
        if result is not None:
            return result.total
        return 0

    @property
    def bit_306(self):
        result = Result.objects.filter(
            student_id=self.id, unit__unit_code='BIT 306').first()
        if result is not None:
            return result.total
        return 0

    @property
    def total(self):
        return self.bit_306 + self.bit_145 + self.bit_141 + self.bit_123 + self.bit_121 + self.bit_113 + self.bit_111
    
    @property
    def grade(self):
        grade = ''
        avg = self.total / 7
        if avg >= 75:
            grade = 'A'
        elif avg >= 65 and avg <= 75:
            grade = 'B'
        elif avg >= 55 and avg <= 64:
            grade = 'C'
        elif avg >= 40 and avg <= 54:
            grade = 'D'
        elif avg >= 0 and avg <= 39:
            grade = 'E'
        return grade

    @property
    def fee_balance(self):
        fee = self.fee_set.all().first()
        return fee.balance
