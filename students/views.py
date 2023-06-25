from django.shortcuts import render

from students.models import Student


# Create your views here.
def get_all(request):
    students = Student.objects.all()
    return render(request, "students/students.html", {"students": students})
