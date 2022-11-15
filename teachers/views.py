from django.shortcuts import render
from .models import Teacher
# Create your views here.
def teachers(request):
    teachers = Teacher.objects.all()
    context = {
        "teachers": teachers
    }
    return render(request, "teachers/teachers.html", context)
