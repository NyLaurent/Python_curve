from django.shortcuts import render
from .models import Course, Enrollment


def dashboard(request):
    courses = Course.objects.all().order_by("code")
    enrollments = Enrollment.objects.select_related("student", "course")
    stats = {
        "num_courses": courses.count(),
        "num_enrollments": enrollments.count(),
    }
    return render(request, "courses/dashboard.html", {
        "courses": courses,
        "enrollments": enrollments[:50],
        "stats": stats,
    })

from django.shortcuts import render

# Create your views here.
