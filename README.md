# 🧳 Job Portal Website

A fully functional Job Portal built with **Django**, styled using **Bootstrap**, and powered by **MySQL**. This platform allows job seekers to apply for jobs and employers to post job openings.

## 🚀 Features

- 👤 **User Roles**: Job Seeker & Employer
- 📄 **Job Postings**: Employers can add jobs
- 🔍 **Job Listings**: Job seekers can view and filter jobs
- 📎 **Apply to Jobs**: Upload resume to apply
- 🗂️ **MySQL Database**: Stores jobs, applications, and user data
- 🎨 **Bootstrap Styling**: Clean responsive UI
- ⚙️ **Django Admin Panel** (optional): Manage data easily

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap, jQuery
- **Backend**: Python, Django
- **Database**: MySQL
- **Others**: Django Templates, File Uploads

## 📦 Installation

```bash
git clone https://github.com/yourusername/jobportal.git
cd jobportal
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## ⚙️ MySQL Configuration

Create a MySQL database:

```sql
CREATE DATABASE job_portal;
```

In `jobportal/settings.py`, update the DB settings:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'job_portal',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## 🔧 Migrate and Run

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📂 Project Structure

```
jobportal/
├── jobs/                # App for job logic
├── templates/           # HTML templates
├── static/              # Bootstrap and custom CSS
├── manage.py
└── jobportal/           # Project settings
```

## ✨ Future Enhancements

- User registration/login
- Search and filter jobs
- Employer dashboard
- Email notifications