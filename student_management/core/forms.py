from django import forms
from .models import Student, Attendance,Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']

