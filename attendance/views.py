from django.shortcuts import render
from .models import Attendence


def attendance_list(request):
    records = Attendence.objects.select_related('student').order_by('-date')
    return render(request, 'attendance/attendance_list.html', { 'records': records })