from django.db.models import Count
from .models import Attendance
from .forms import AttendanceForm
import matplotlib.pyplot as plt
import io
import urllib, base64
from django.shortcuts import render, redirect
from .models import Department, Course, Student, Faculty
from .forms import DepartmentForm, CourseForm, StudentForm, FacultyForm

def home(request):
    return render(request, 'college/home.html')

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'college/department_list.html', {'departments': departments})

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'college/department_form.html', {'form': form})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'college/course_list.html', {'courses': courses})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'college/course_form.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'college/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'college/student_form.html', {'form': form})

def faculty_list(request):
    faculties = Faculty.objects.all()
    return render(request, 'college/faculty_list.html', {'faculties': faculties})

def faculty_create(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
    else:
        form = FacultyForm()
    return render(request, 'college/faculty_form.html', {'form': form})



def attendance_list(request, course_id=None):
    if course_id:
        attendances = Attendance.objects.filter(course_id=course_id)
    else:
        attendances = Attendance.objects.all()
    return render(request, 'college/attendance_list.html', {'attendances': attendances})

def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'college/attendance_form.html', {'form': form})

def attendance_stats(request, course_id):
    # Get attendance data
    stats = Attendance.objects.filter(course_id=course_id).values('status').annotate(count=Count('status'))
    
    # Prepare data for chart
    labels = []
    sizes = []
    for item in stats:
        labels.append(dict(Attendance.STATUS_CHOICES)[item['status']])
        sizes.append(item['count'])
    
    # Create pie chart
    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle
    plt.title('Attendance Distribution')
    
    # Convert plot to image
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    
    return render(request, 'college/attendance_stats.html', {
        'graphic': graphic,
        'course': Course.objects.get(id=course_id)
    })