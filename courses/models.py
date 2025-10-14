from django.db import models
from attendance.models import Student  # reuse your existing Student

class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "course"

    def __str__(self):
        return f"{self.code} - {self.title}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")

    class Meta:
        db_table = "enrollment"
        unique_together = ("student", "course")

    def __str__(self):
        return f"{self.student.name} -> {self.course.code}"