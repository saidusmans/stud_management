from core.models import Student, Course
import random
from datetime import date, timedelta

names = ["Aarav", "Diya", "Rahul", "Sneha", "Karan", "Ishita", "Aditya", "Meera", "Rohan", "Neha"]
courses = list(Course.objects.all())

def random_dob():
    # Random date between 18 and 25 years old
    start_date = date.today() - timedelta(days=25*365)
    end_date = date.today() - timedelta(days=18*365)
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

used_rolls = set(Student.objects.values_list("roll_no", flat=True))

for i, name in enumerate(names, start=1):
    course = random.choice(courses)
    dob = random_dob()

    # Ensure roll_no is unique
    roll_no = f"STU{1000 + i}"
    while roll_no in used_rolls:
        i += 1
        roll_no = f"STU{1000 + i}"

    used_rolls.add(roll_no)

    student, created = Student.objects.get_or_create(
        name=name,
        roll_no=roll_no,
        course=course,
        date_of_birth=dob
    )
    print(f"{'Created' if created else 'Exists'}: {student.name} - {student.roll_no} - {student.course.name}")
