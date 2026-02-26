from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "mydb"),
        user=os.environ.get("DB_USER", "myuser"),
        password=os.environ.get("DB_PASSWORD", "mypassword")
    )
    return conn

@app.route("/")
def index():
    try:
        conn = get_db_connection()
        conn.close()
        return "<h1>Flask + PostgreSQL is working!</h1><p>Database connection successful ✅</p>"
    except Exception as e:
        return f"<h1>Database connection failed ❌</h1><p>{e}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)