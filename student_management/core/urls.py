from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='course_list'),
    path('students/', views.student_list, name='student_list'),
    path('register/', views.student_register, name='student_register'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
]
