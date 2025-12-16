# 📚 Student Management System (Django)

A **Django-based Student Management System** designed to manage students, assign courses, and track attendance efficiently. This project is built for learning and demonstration purposes and highlights core Django concepts such as models, views, templates, forms, and the ORM.

---

## 🚀 Features

### 👨‍🎓 Student Management

* Add, update, and delete student records
* Assign students to one or more courses

### 📘 Course Management

* Create and manage courses
* View students enrolled in each course

### 📝 Attendance Tracking

* Mark daily attendance for students
* View attendance records on a dedicated page

### 🔐 Admin Panel

* Manage students, courses, and attendance via Django Admin

### 🎨 User Interface

* Simple and clean UI
* Easy navigation between modules

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite (default)
* **Tools:** Django ORM, Django Admin

---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/saidusmans/stud_management.git
   cd stud_management
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Open in browser**

   * Application: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   * Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📂 Project Structure

```
stud_management/
│
├── student_management/    # Main Django app
├── vr/                    # Additional Django app
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS, Images)
├── manage.py              # Django management script
└── requirements.txt       # Project dependencies
```

---

## 📸 Screenshots (Optional)

* Student list page
* Course management page
* Attendance page

---

## 🎯 Learning Outcomes

* Understanding Django models and relationships
* Working with forms and templates
* Implementing CRUD operations
* Managing attendance logic

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
