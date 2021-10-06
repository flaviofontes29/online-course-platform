from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import Courses


def home(request):
    if request.session.get("user"):
        course = Courses.objects.all()
        request_user = request.session.get("user")
        return render(
            request, "home.html", {"course": course, "request_usuario": request_user}
        )
    else:
        return redirect("/auth/login/?status=2")
