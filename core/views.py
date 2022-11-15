from django.shortcuts import render
from students.models import Student
from teachers.models import Teacher

# Create your views here.
def home(request):
    return render(request, "home.html")

def marksheet(request):
    students = Student.objects.all()
    context = {
        "students": students
    }
    return render(request, "marksheet.html", context)