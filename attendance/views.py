from django.shortcuts import render
from .models import Attendence, Student
from .forms import StudentForm
from django.shortcuts import render, redirect
from django.utils import timezone


def attendance_list(request):
    records = Attendence.objects.select_related('student').order_by('-date')
    return render(request, 'attendance/attendance_list.html', { 'records': records })



def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance:attendance_list')
        # If form is invalid, render the form again with errors
        return render(request, 'attendance/add_student.html', {'form': form})
    else:
        form = StudentForm()
        return render(request, 'attendance/add_student.html', {'form': form})







def mark_attendance(request):
    students = Student.objects.all()
    date = timezone.now().date()

    if request.method == 'POST':
        for student in students:
            is_present = request.POST.get(f'student_{student.id}') == 'on'
            Attendence.objects.update_or_create(
                student=student,
                date=date,
                defaults={ 'present': is_present }
            )
        return redirect('attendance:attendance_list')

    return render(request, 'attendance/mark_attendance.html', {
        'students': students,
        'date': date,
    })