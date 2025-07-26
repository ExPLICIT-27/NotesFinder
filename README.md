# 📝 NotesFinder

A web-based platform to help students quickly find, favorite, and access academic notes based on subjects, topics, and keywords. Built using **Django** for the backend and **HTML/CSS/JavaScript** for the frontend.

---


## 🚀 Features

- 🔍 **Instant Search**: Search for notes using keywords or abbreviations (e.g., "cvla" for "Complex Variables and Linear Algebra")
- 📁 **Subject-wise Organization**: Each subject has a dedicated, styled page
- ⭐ **Favorites**: Users can favorite notes or subjects and access them quickly
- 🔐 **User Authentication**: Register and log in to personalize your experience
- 🖼️ **Profile Management**: Change profile picture and update user details
- 📄 **Clean UI**: Responsive and user-friendly design using modern CSS

---

## 🏗️ Tech Stack

| Layer        | Technology |
|--------------|------------|
| Backend      | Django (Python) |
| Frontend     | HTML, CSS, JavaScript |
| Styling      | Custom CSS (Dark Mode supported) |
| Database     | SQLite (default, can switch to PostgreSQL) |
| Auth         | Django built-in authentication system |

---

---

## ⚙️ Setup Instructions

### 1. Clone the repository, then
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.
