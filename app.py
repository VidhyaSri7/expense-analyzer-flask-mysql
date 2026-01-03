from flask import Flask, render_template, request, redirect, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# ---------- Database Connection ----------
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# ---------- Routes ----------

@app.route("/", methods=["GET", "POST"])
def login():
    cursor = db.cursor(dictionary=True)

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        cursor.execute(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )
        user = cursor.fetchone()
        cursor.close()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            return redirect("/dashboard")
        else:
            return "Invalid credentials"

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    cursor = db.cursor(dictionary=True)

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])

        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, password)
        )
        db.commit()
        cursor.close()
        return redirect("/")

    cursor.close()
    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/")

    user_id = session["user_id"]
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT IFNULL(SUM(amount),0) AS income FROM transactions WHERE user_id=%s AND type='income'",
        (user_id,)
    )
    total_income = cursor.fetchone()["income"]

    cursor.execute(
        "SELECT IFNULL(SUM(amount),0) AS expense FROM transactions WHERE user_id=%s AND type='expense'",
        (user_id,)
    )
    total_expense = cursor.fetchone()["expense"]

    balance = total_income - total_expense

    cursor.execute("""
        SELECT category, SUM(amount) AS total
        FROM transactions
        WHERE user_id=%s AND type='expense'
        GROUP BY category
    """, (user_id,))
    data = cursor.fetchall()

    categories = [row["category"] for row in data]
    totals = [float(row["total"]) for row in data]

    cursor.close()

    return render_template(
        "dashboard.html",
        total_income=total_income,
        total_expense=total_expense,
        balance=balance,
        categories=categories,
        totals=totals
    )


@app.route("/add", methods=["GET", "POST"])
def add():
    if "user_id" not in session:
        return redirect("/")

    user_id = session["user_id"]
    cursor = db.cursor(dictionary=True)

    if request.method == "POST":
        amount = float(request.form["amount"])
        category = request.form["category"]
        date = request.form["date"]
        description = request.form["description"]
        trans_type = request.form["type"]

        cursor.execute("""
            INSERT INTO transactions
            (user_id, amount, category, trans_date, description, type)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (user_id, amount, category, date, description, trans_type))

        db.commit()
        cursor.close()
        return redirect("/dashboard")

    cursor.close()
    return render_template("add_expense.html")


@app.route("/transactions")
def transactions():
    if "user_id" not in session:
        return redirect("/")

    user_id = session["user_id"]
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM transactions WHERE user_id=%s ORDER BY trans_date DESC",
        (user_id,)
    )
    data = cursor.fetchall()
    cursor.close()

    return render_template("transactions.html", transactions=data)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
