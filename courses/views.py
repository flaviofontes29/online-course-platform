from django.shortcuts import redirect, render
from django.http import HttpResponse


def home(request):
    if request.session.get("user"):
        pass
        pass
        return HttpResponse("Estou na pagina home")
    else:
        return redirect("/auth/login?status=2")
