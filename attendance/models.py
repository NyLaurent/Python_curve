from django.db import models
from django.utils import timezone


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    RESIDENCE_CHOICES = [
        ('school', 'Lives in School'),
        ('outside', 'Lives Outside School'),
    ]
    
    name = models.CharField(max_length=100)
    classroom = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    residence = models.CharField(max_length=10, choices=RESIDENCE_CHOICES, default='school')

    class Meta:
        db_table = "student"

    def __str__(self):
        return f"{self.name} - {self.classroom}"


class Attendence(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    present = models.BooleanField(default=False)

    class Meta:
        db_table = "attendence"

    def __str__(self):
        return f"{self.student.name} - {self.date} - {'Present' if self.present else 'Absent'}"
