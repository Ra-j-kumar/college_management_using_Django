from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.department_create, name='department_create'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_create, name='course_create'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_create, name='student_create'),
    path('faculty/', views.faculty_list, name='faculty_list'),
    path('faculty/add/', views.faculty_create, name='faculty_create'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/add/', views.attendance_create, name='attendance_create'),
    path('attendance/course/<int:course_id>/', views.attendance_list, name='course_attendance'),
    path('attendance/stats/<int:course_id>/', views.attendance_stats, name='attendance_stats'),
]