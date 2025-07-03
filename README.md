#  Student Result System with Role-Based Access Control (RBAC)

This project is a secure, web-based application built using **Flask (Python)** to manage student results within an educational institution. It applies **Role-Based Access Control (RBAC)** to ensure that users—**Admin**, **Teacher**, and **Student**—only have access to features appropriate for their role. It provides a simple, scalable solution for result tracking in schools or colleges.


##  Project Overview:
The Student Result System is designed to simulate a real-world academic platform where users interact based on their assigned responsibilities. The application is fully functional with individual dashboards for each role and enables:

- Admins to manage user accounts (teachers and students)
- Teachers to submit and view marks
- Students to view their own academic results securely

This project focuses on key concepts such as **authentication**, **authorization**, **CRUD operations**, and **secure session handling**, making it an excellent educational tool and a strong addition to a technical portfolio.


##  Project Description:
This system demonstrates the concept of RBAC by segregating user access and functionality. All users log in via a single login page, and the application automatically redirects them to their specific dashboard based on their role:

- **Admins** can add, update, and delete teachers and students.
- **Teachers** can input student marks for different subjects and view all submissions.
- **Students** can view only their personal marks.

The application is built with simplicity and security in mind. Passwords can be updated by each user from their profile, and the UI is designed using **Bootstrap** for responsiveness and ease of use.


##  User Roles and Access Rights:
Role separation is at the heart of this application. Each user has limited visibility and control based on their role to prevent unauthorized actions or data exposure.

###  Role Permissions

| Role          | Permissions 

| **Admin**      - Secure login  
                 - Add new teachers and students  
                 - Edit and delete user details  
                 - View all user records  
                 - Access admin-only features 

| **Teacher**    - Secure login  
                 - Submit and view marks for students  
                 - View all result entries  
                 - Update personal password 

| **Student**    - Secure login  
                 - View personal academic performance  
                 - Update own password from profile |


##  Key Features:

### 1.  Role-Based Access Control
Each user is redirected to a custom dashboard based on their assigned role, ensuring restricted and secure access to functionalities.

### 2.  Admin Management Panel
Admins have full control over user accounts—adding, editing, or removing teacher and student users directly from the dashboard.

### 3.  Teacher Result Portal
Teachers can select a student, choose a subject, and submit marks. They can also view a full list of submitted results.

### 4.  Student Result Viewer
Students can log in and see a clear display of all their subject-wise marks. No access is given to results of other students.

### 5.  Profile Management
All users can change their password securely through the "Profile" page, which is accessible by clicking on their name in the navigation bar.


##  Application Workflow

Here’s how the system functions from a user experience perspective:

1. **User Login**
   - Each user logs in with a unique `login ID` and `password`.

2. **Authentication**
   - The system validates credentials and checks the user role from the database.

3. **Role-Based Redirection**
   - Users are sent to the appropriate dashboard: Admin, Teacher, or Student.

4. **Dashboard Actions**
   - Based on role, users perform specific tasks:
     - Admin: Manage users
     - Teacher: Submit and view results
     - Student: View personal results

5. **Profile Access**
   - All users can click on their name in the navbar to access the profile page to change passwords.

6. **Logout**
   - Ends the session securely and redirects back to the login screen.


##  Technologies Used

This project uses lightweight and widely adopted tools for simplicity and ease of deployment:

| Layer         | Technology                     |
|-------------- |------------------------------- |
| **Frontend**  | HTML5, CSS3, Bootstrap, Jinja2 |
| **Backend**   | Python 3.x, Flask              |
| **Database**  | SQLite (lightweight RDBMS)     |
| **Versioning**| Git, GitHub                    |


##  Project Structure
RBAC_Student_Result_System/
├── app.py
├── templates/
│ ├── login.html
│ ├── admin_dashboard.html
│ ├── teacher_dashboard.html
│ ├── student_dashboard.html
│ ├── edit_user.html
│ ├── profile.html
├── database.db # auto-generated
└── README.md



##  Default Login Credentials

| Role     | Login ID | Password  |
|----------|----------|-----------|
| Admin    | admin01  | admin123  |
| Teacher  | T001     | pass123   |
| Student  | S001     | pass321   |


##  Database Overview

### `users` Table
- `id`: Integer (Primary Key)
- `name`: Text
- `role`: Text ('admin', 'teacher', 'student')
- `login_id`: Text (unique username)
- `password`: Text (plain for demo)

### `results` Table
- `id`: Integer (Primary Key)
- `student_id`: Text
- `subject`: Text
- `marks`: Integer
- `teacher_id`: Text


##  Getting Started (How to Run Locally)

1. **Install Flask**
pip install flask

2. **Run the App**
python app.py

3. **Open in the browser by generated https link**

# screen shots


# Future Improvements
Add pagination, filters, and sorting for result tables

Enable PDF download of marksheets

Graphical analytics of performance

Deploy live using PythonAnywhere or Render

Encrypt passwords (not plain text)

password management

opt generation for more security


# Use Cases
This system is designed with real-world academic and educational workflows in mind. Below are several practical scenarios where this project can be effectively applied or extended:

1. School/College Result Management System

2. Learning Management System (LMS) Component

3. Demo for Role-Based Access Control (RBAC)

4. Portfolio Project for Resume/GitHub

5. Internal Tool for Training Institutes or Coaching Centers

6. Starter Project for Full-Stack Flask Applications

# Acknowledgments
Built with using:

Python & Flask

SQLite

Bootstrap

The open-source community