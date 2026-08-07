from flask import Flask, render_template, request, redirect, url_for, session
from ceaser_ciph import run_cipher
from password_generator import run_password_genrator
from port_scan import run_scanner
import hashlib
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"

def create_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL UNIQUE)
    """)

    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS passwords(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL)
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS portscan(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        openports REAL NOT NULL UNIQUE)
    """)
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def home():
    if "user" in session:
        return redirect(url_for("welcome"))

    if request.method == "POST":
        username = request.form["username"].lower()
        password = request.form["password"]
        hashed = hashlib.sha256(password.encode()).hexdigest()

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",
                      (username, hashed))
        result = cursor.fetchone()
        conn.close()

        if result:
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return render_template("home.html", error="Invalid credentials")

    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if "user" in session:
        return redirect(url_for("welcome"))

    if request.method == "POST":
        username = request.form["username"].lower()
        password = request.form["password"]
        hashed = hashlib.sha256(password.encode()).hexdigest()

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                          (username, hashed))
            conn.commit()
            return redirect(url_for("home"))
        except:
            return render_template("register.html", error="Username already exists")
        finally:
            conn.close()

    return render_template("register.html")

@app.route("/welcome")
def welcome():
    if "user" not in session:
        return redirect(url_for("home"))
    return render_template("welcome.html")

@app.route("/ceaser_cipher", methods=["GET","POST"])
def ceaser_cipher():
    if "user" not in session:
        return redirect(url_for("home"))
    

    if request.method == "POST":
        message = request.form["message"]
        key = int(request.form["key"])
        choice = request.form["choice"]
        result = run_cipher(message,key,choice)
        return render_template("ceaser_cipher.html", result=result)
    return render_template("ceaser_cipher.html")

@app.route("/password_generator", methods=["GET", "POST"])
def password_generator():
    if "user" not in session:
        return redirect(url_for("home"))

    if request.method == "POST":
        
        quantity = int(request.form["quantity"])
        length = int(request.form["length"])
        passwords = run_password_genrator(length, quantity)

        conn =sqlite3.connect("users.db")
        cursor = conn.cursor()
        for password in passwords:
            cursor.execute("""INSERT INTO passwords (username, password) 
                           VALUES(?, ?)""",
                           (session["user"], password)
                        )
        conn.commit()
        conn.close()
            
    conn =sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
            SELECT password FROM passwords WHERE username = ?""",
            (session["user"],))
    results = cursor.fetchall()
    conn.close()
        
    return render_template("password_generator.html",results=results)

@app.route("/port_scanner", methods=["GET", "POST"])
def port_scanner():
    if "user" not in session:
        return redirect(url_for("home"))
    if request.method == "POST":
        target = request.form["target"]
        start_port = int(request.form["start_port"])
        end_port = int(request.form["end_port"])
        openports = run_scanner(target, start_port, end_port)
        open_ports_str = ",".join(str(p) for p in openports)

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("""
                INSERT INTO portscan (username, openports) 
                VALUES (?, ?)""", (session["user"], open_ports_str))
        conn.commit()
        conn.close()
    conn =sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT openports FROM portscan WHERE username =?""",
        (session["user"],))
    results = cursor.fetchall()
    conn.close()
    return render_template("port_scanner.html", results=results)
    


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

create_table()

if __name__ == "__main__":
    app.run(debug=True)