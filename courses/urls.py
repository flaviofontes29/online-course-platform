from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("course/<int:id>", views.course, name="course"),
    path("class/<int:id>", views.class_, name="class"),
]
