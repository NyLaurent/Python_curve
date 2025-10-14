from django.contrib import admin
from .models import Course, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "title")
    search_fields = ("code", "title")

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course")
    list_filter = ("course",)
    search_fields = ("student__name", "course__code")
    autocomplete_fields = ("student", "course")