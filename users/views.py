from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.shortcuts import redirect
import hashlib


def registration(request):
    if request.session.get("user"):
        redirect("/home")

    status = request.GET.get("status")
    return render(request, "registration.html", {"status": status})


def login(request):
    if request.session.get("user"):
        redirect("/home")
    status = request.GET.get("status")
    return render(request, "login.html", {"status": status})


def valid_registry(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    password = request.POST.get("password")
    user_exists = User.objects.filter(email=email)

    if len(name.strip()) == 0 or len(email.strip()) == 0:
        return redirect("/auth/registration/?status=2")

    if len(user_exists) > 0:
        return redirect("/auth/registration/?status=1")

    if len(password) < 8 or len(password) > 12:
        return redirect("/auth/registration/?status=3")
    try:
        password = hashlib.sha256(password.encode()).hexdigest()
        user = User(name=name, email=email, password=password)
        user.save()
    except Exception:
        return redirect("/auth/cadastro/?status=4")
    return redirect("/auth/registration/?status=0")


def valid_login(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    password = hashlib.sha256(password.encode()).hexdigest()
    users = User.objects.filter(email=email).filter(password=password)
    if len(users) == 0:
        return redirect("/auth/login/?status=1")
    elif len(users) > 0:
        request.session["user"] = users[0].id
        return redirect("/home")


def logout(request):
    request.session.flush()
    return redirect("/auth/login")
