# 📝 Notebook Web App

A simple and clean notebook web application built with Flask that allows users to **add, edit, and delete notes** بسهولة.

---

## 🚀 Features

* ➕ Add new notes
* ✏️ Edit existing notes
* ❌ Delete notes
* 💾 Data stored باستخدام MySQL Database
* 🌐 واجهة بسيطة باستخدام HTML & CSS
* 🔄 Dynamic rendering باستخدام Jinja

---

## 🛠️ Technologies Used

* Python (Flask Framework)
* SQLAlchemy (ORM)
* MySQL Database
* HTML5
* CSS3
* Jinja2

---

## 📂 Project Structure

```
notebook/
│
├── app.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/notebook.git
cd notebook
```

### 2. Create virtual environment (optional but recommended)

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install flask sqlalchemy pymysql
```

### 4. Configure Database

* تأكد إن MySQL شغال عندك
* أنشئ Database جديدة (مثلاً: notebook_db)

### 5. Run the app

```
python app.py
```

---

## 🧠 How It Works

* Flask handles routing and backend logic
* SQLAlchemy manages database operations
* MySQL stores notes data
* Jinja renders dynamic HTML pages

---

## 📸 Screenshots

(ضيف صور للمشروع هنا لو حابب)

---

## 📌 Future Improvements

* User authentication (login/register)
* Search functionality
* Categories for notes
* Dark mode 🌙

---

## 👨‍💻 Author

Your Name

---

## 📄 License

This project is open-source and free to use.
