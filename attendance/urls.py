from django.urls import path
from . import views


app_name = "attendance"


urlpatterns = [
    path("", views.attendance_list, name="attendance_list"),
    path("add-student/", views.add_student, name="add_student"),
    path("mark-attendance/", views.mark_attendance, name="mark_attendance"),
]


