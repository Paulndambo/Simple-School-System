from django.db import models

# Create your models here.
class Unit(models.Model):
    unit_code = models.CharField(max_length=255)
    unit_title = models.CharField(max_length=255)
    current_lecturer = models.ForeignKey(to="teachers.Teacher", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.unit_code


class Result(models.Model):
    student = models.ForeignKey(to="students.Student", on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    cat = models.FloatField(default=0)
    exam = models.FloatField(default=0)
    total = models.FloatField(null=True, blank=True)

    def save(self):
        self.total = self.cat + self.exam
        return super().save()

    def __str__(self):
        return self.student.name

    