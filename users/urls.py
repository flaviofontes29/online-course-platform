from django.urls import path
from . import views


urlpatterns = [
    path("registration/", views.registration, name="registration"),
    path("login/", views.login, name="login"),
    path("valid_registry", views.valid_registry, name="valid_registry"),
]
