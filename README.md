# 📘 **Barangay Environmental Monitoring and Reporting System — Padre Garcia, Batangas**

A community-based web application for reporting, monitoring, and managing environmental issues within the Municipality of Padre Garcia, Batangas.
Developed by **BSIT 2103 – Group 3** (Batangas State University – The National Engineering University)

---

# 🚀 **Project Overview**

The **Barangay Environmental Monitoring and Reporting System** is a web platform that enables residents to conveniently report environmental issues—such as garbage pile-ups, flooding, pollution, vandalism, broken public facilities, and more.
The system supports:

* **User report submission**
* **Photo uploads**
* **Automatic status tracking**
* **Admin management dashboard**
* **Report filtering**
* **Environmental awareness**

This project aims to strengthen citizen participation and improve the efficiency of barangay environmental response and governance.

---

# 🌍 **Sustainable Development Goals Alignment**

This system directly supports:

* **SDG 3 – Good Health and Well-Being**
* **SDG 11 – Sustainable Cities and Communities**
* **SDG 15 – Life on Land**

By encouraging proper waste management, improving environmental reporting, and fostering community responsibility, the system helps create a cleaner and healthier environment.

---

# 🧩 **System Features**

### 👤 **User Features**

* Submit reports with title, description, category, and exact address
* Upload photos as evidence
* View all submitted reports
* Filter reports by category
* Track report status (Pending → In Progress → Resolved)

### 🔐 **Admin Features**

* Admin login
* View all submitted reports in a dashboard
* Update report status
* Delete inaccurate or duplicate reports
* Manage community feedback efficiently

---

# 🖥 **Tech Stack**

| Layer      | Technology                      |
| ---------- | ------------------------------- |
| Backend    | **Python Flask**                |
| Database   | **PostgreSQL + SQLAlchemy ORM** |
| Frontend   | HTML5, CSS3, Jinja2 Templates   |
| Tools      | Flask-Migrate, Werkzeug, dotenv |
| Deployment | Localhost / Any cloud server    |

---

# 📂 **Project Structure**

```
/project-folder
│── app.py
│── models.py
│── requirements.txt
│── /templates
│── /static
│── /uploads
│── README.md
```

---

# 🧰 **Installation & Setup**

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/eijj-dope/Env.reporting.git
cd Env.reporting
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

Create `.env`:

```
DATABASE_URL=postgresql://postgres:Russelflores2005@localhost:5432/envreportdb
FLASK_SECRET=group-3
USE_SSL=False
ADMIN_PASSWORD=Admin@123
```

### 4️⃣ Run Database Migrations

```bash
flask db upgrade
```

### 5️⃣ Start the Application

```bash
python app.py
```

App runs on:
➡ [http://localhost:5000/](http://localhost:5000/)

---

# 🧾 **Database Design**

### **Tables**

✔ Categories
✔ Statuses
✔ Reports

Structured using **3NF Normalization** to prevent redundancy.

### **Key ERD Tables**

**categories**

```
category_id (PK)
category_name
```

**statuses**

```
status_id (PK)
status_name
```

**reports**

```
id (PK)
title
description
address
photo_url
created_at
updated_at
category_id (FK)
status_id (FK)
```

---

# 🗂 **Sample SQL Queries**

### 👉 Basic SELECT

```sql
SELECT * FROM reports;
```

### 👉 JOIN (Admin Dashboard)

```sql
SELECT r.id, r.title, r.address, r.description,
       c.category_name, s.status_name
FROM reports r
JOIN categories c ON r.category_id = c.category_id
JOIN statuses s ON r.status_id = s.status_id;
```

### 👉 Filtering by Category

```sql
SELECT * FROM reports r
JOIN categories c ON r.category_id = c.category_id
WHERE c.category_name = 'Flood';
```

---

# 📸 **System Pages**

### 🏠 **Home Page**

* Shows system description
* Social links
* Developers section

### 📝 **Submit Report**

Users complete:

* Report Title
* Description
* Category
* Address
* Photo Upload

### 📑 **All Reports**

* Displays all environmental reports
* Users can filter by category
* Tracks status

### 🔐 **Admin Dashboard**

* Admin login
* View all reports
* Update report status
* Delete reports

---

# 🔮 **Future Improvements**

* Mobile app version
* Real-time GPS auto-location
* SMS / Email notifications
* Advanced analytics dashboard
* Two-factor authentication
* Improved admin role permissions

---

# 👨‍💻 **Developers — Group 3**

| Name                              | Role               |
| --------------------------------- | ------------------ |
| **Russel Christian D. Flores**    | Backend Developer  |
| **Jayson G. Belchiz**             | Frontend Developer |
| **Valerie Kristine A. Taberdo**   | Documentation Lead |
| **Nathapon Danielle M. Thongtam** | Research Lead      |

---

# 🏁 **Conclusion**

This project showcases how digital solutions can significantly enhance environmental reporting, monitoring, and barangay response. By enabling residents to submit reports easily and providing admins with efficient management tools, the system strengthens community participation and helps create a cleaner and safer environment for Padre Garcia, Batangas.

