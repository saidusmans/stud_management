from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

class Attendance(models.Model):
    STATUS_CHOICES = [('Present', 'Present'), ('Absent', 'Absent')]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"
