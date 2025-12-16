from email.mime import image
import os
from datetime import date 
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Course, Student, Attendance
from .forms import StudentForm, AttendanceForm

# Helper function to save attendance records to a file
def save_attendance_to_file(selected_date):
    # Get attendance for the given date
    attendance_records = Attendance.objects.filter(date=selected_date)

    # Create folder path for attendance files
    folder_path = os.path.join(settings.BASE_DIR, 'attendance_records')
    os.makedirs(folder_path, exist_ok=True)

    # Create a file named with the date (e.g., 2025-08-27.txt)
    file_path = os.path.join(folder_path, f"{selected_date}.txt")

    # Write attendance data to the file
    with open(file_path, 'w') as f:
        for record in attendance_records:
            f.write(f"{record.student.name} - {record.status}\n")

# Home Page View with Dynamic Stats
def home(request):
    students_count = Student.objects.count()
    courses_count = Course.objects.count()
    attendance_count = Attendance.objects.count()
    context = {
        'students_count': students_count,
        'courses_count': courses_count,
        'attendance_count': attendance_count,
    }
    return render(request, 'core/home.html', context)

# View All Courses
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'core/course_list.html', {'courses': courses})

# View All Students
# views.py

def student_list(request):
    query = request.GET.get('q', '')  # get search input
    if query:
        students = Student.objects.filter(
            roll_no__icontains=query
        ) | Student.objects.filter(
            name__icontains=query
        )
    else:
        students = Student.objects.none()

    return render(request, 'core/student_list.html', {'students': students, 'query': query})

# Register New Student
def student_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'core/student_form.html', {'form': form})

# View Attendance Records by Date
def attendance_list(request):
    # Get date from query parameter or default to today
    selected_date = request.GET.get('date', date.today().isoformat())
    records = Attendance.objects.filter(date=selected_date).order_by('-date')

    # Save attendance for this date into a file
    save_attendance_to_file(selected_date)

    return render(request, 'core/attendance_list.html', {
        'attendance': records,
        'selected_date': selected_date
    })

# Mark Attendance
def mark_attendance(request):
    students = Student.objects.all()
    today = date.today()

    if request.method == 'POST':
        attendance_data = request.POST  # Get POST data
        for student in students:
            status = 'Present' if attendance_data.get(f'student_{student.id}') else 'Absent'
            Attendance.objects.update_or_create(
                student=student,
                date=today,
                defaults={'status': status}
            )
        # After saving, stay on the same page (not redirecting)
        return render(request, 'core/attendance_form.html', {
            'students': students,
            'success': True
        })

    return render(request, 'core/attendance_form.html', {'students': students})
