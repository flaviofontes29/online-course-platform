from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ("name", "email")
    readonly_fields = ("password",)
