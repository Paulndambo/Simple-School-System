from django.shortcuts import render
from .models import Student
# Create your views here.
def students(request):
    students = Student.objects.all()
    context = {
        "students": students
    }
    return render(request, "students/students.html", context)