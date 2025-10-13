from django.contrib import admin
from .models import Student, Attendence


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "classroom")
    list_filter = ("classroom",)
    search_fields = ("name",)


@admin.register(Attendence)
class AttendenceAdmin(admin.ModelAdmin):
    list_display = ("date", "student", "present")
    list_filter = ("present", "date")
    search_fields = ("student__name",)
