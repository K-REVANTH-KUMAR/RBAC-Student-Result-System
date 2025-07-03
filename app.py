from flask import Flask, render_template, request, redirect, session, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'secret_key'

# --- DATABASE SETUP ---
if not os.path.exists('database.db'):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        role TEXT,
        login_id TEXT UNIQUE,
        password TEXT
    )''')

    # Create results table
    cursor.execute('''CREATE TABLE results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT,
        subject TEXT,
        marks INTEGER,
        teacher_id TEXT
    )''')

    # Insert sample users
    cursor.execute("INSERT INTO users (name, role, login_id, password) VALUES (?, ?, ?, ?)",
                   ("Admin", "admin", "admin01", "admin123"))
    cursor.execute("INSERT INTO users (name, role, login_id, password) VALUES (?, ?, ?, ?)",
                   ("Alice", "teacher", "T001", "pass123"))
    cursor.execute("INSERT INTO users (name, role, login_id, password) VALUES (?, ?, ?, ?)",
                   ("Bob", "student", "S001", "pass321"))

    conn.commit()
    conn.close()

# --- ROUTES ---
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_id = request.form['login_id']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE login_id=? AND password=?", (login_id, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['login_id'] = user[3]
            session['role'] = user[2]
            session['name'] = user[1]

            if user[2] == 'admin':
                return redirect('/admin')
            elif user[2] == 'teacher':
                return redirect('/teacher')
            elif user[2] == 'student':
                return redirect('/student')
        else:
            flash("Invalid credentials", "danger")

    return render_template('login.html')

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if 'login_id' not in session:
        return redirect('/')

    if request.method == 'POST':
        old = request.form['old_password']
        new = request.form['new_password']
        confirm = request.form['confirm_password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE login_id=?", (session['login_id'],))
        current_pw = cursor.fetchone()[0]

        if old != current_pw:
            flash("Old password is incorrect", "danger")
        elif new != confirm:
            flash("New passwords do not match", "danger")
        else:
            cursor.execute("UPDATE users SET password=? WHERE login_id=?", (new, session['login_id']))
            conn.commit()
            flash("Password changed successfully!", "success")

        conn.close()

    return render_template('change_password.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'login_id' not in session:
        return redirect('/')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, role, login_id FROM users WHERE login_id=?", (session['login_id'],))
    user = cursor.fetchone()

    if request.method == 'POST':
        old = request.form['old_password']
        new = request.form['new_password']
        confirm = request.form['confirm_password']

        cursor.execute("SELECT password FROM users WHERE login_id=?", (session['login_id'],))
        current_pw = cursor.fetchone()[0]

        if old != current_pw:
            flash("Old password is incorrect", "danger")
        elif new != confirm:
            flash("New passwords do not match", "danger")
        else:
            cursor.execute("UPDATE users SET password=? WHERE login_id=?", (new, session['login_id']))
            conn.commit()
            flash("Password updated successfully!", "success")

    conn.close()
    return render_template('profile.html', user=user)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'role' not in session or session['role'] != 'admin':
        return redirect('/')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        login_id = request.form['login_id']
        password = request.form['password']

        cursor.execute("INSERT INTO users (name, role, login_id, password) VALUES (?, ?, ?, ?)",
                       (name, role, login_id, password))
        conn.commit()
        flash("User added successfully!", "success")

    cursor.execute("SELECT * FROM users WHERE role != 'admin'")
    users = cursor.fetchall()
    conn.close()

    return render_template('admin_dashboard.html', users=users)

@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if 'role' not in session or session['role'] != 'admin':
        return redirect('/')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        login_id = request.form['login_id']
        password = request.form['password']
        cursor.execute("UPDATE users SET name=?, role=?, login_id=?, password=? WHERE id=?",
                       (name, role, login_id, password, user_id))
        conn.commit()
        conn.close()
        flash("User updated successfully!", "success")
        return redirect('/admin')

    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return render_template('edit_user.html', user=user)

@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    if 'role' not in session or session['role'] != 'admin':
        return redirect('/')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    flash("User deleted successfully!", "success")
    return redirect('/admin')

@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
    if 'role' not in session or session['role'] != 'teacher':
        return redirect('/')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        student_id = request.form['student_id']
        subject = request.form['subject']
        marks = request.form['marks']
        teacher_id = session['login_id']

        cursor.execute("INSERT INTO results (student_id, subject, marks, teacher_id) VALUES (?, ?, ?, ?)",
                       (student_id, subject, marks, teacher_id))
        conn.commit()
        flash("Result added successfully!", "success")

    cursor.execute("SELECT * FROM users WHERE role = 'student'")
    students = cursor.fetchall()
    cursor.execute("SELECT * FROM results")
    results = cursor.fetchall()
    conn.close()

    return render_template('teacher_dashboard.html', students=students, results=results)

@app.route('/student')
def student():
    if 'role' not in session or session['role'] != 'student':
        return redirect('/')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT subject, marks FROM results WHERE student_id=?", (session['login_id'],))
    results = cursor.fetchall()
    conn.close()

    return render_template('student_dashboard.html', results=results)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
