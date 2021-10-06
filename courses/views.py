from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Courses, Classes


def home(request):
    if request.session.get("user"):
        courses = Courses.objects.all()
        request_user = request.session.get("user")
        return render(
            request, "home.html", {"courses": courses, "request_usuario": request_user}
        )
    else:
        return redirect("/auth/login/?status=2")


def course(request, id):
    id_course = Courses.objects.get(id=id)
    classes = Classes.objects.filter(course=id_course)
    return render(request, "course.html", {"classes": classes})
