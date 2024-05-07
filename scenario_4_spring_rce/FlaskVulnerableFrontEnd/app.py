import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, info TEXT)')
    conn.execute('CREATE TABLE IF NOT EXISTS secrets (id INTEGER PRIMARY KEY, secret_info TEXT)')
    conn.execute('INSERT INTO data (info) VALUES ("Sample 1"), ("Sample 2"), ("Sample 3")')
    conn.execute('INSERT INTO secrets (secret_info) VALUES ("API_KEY:12345XYZ"), ("Internal URL:http://localhost:8090/entity/1")')
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return 'Welcome to the Vulnerable Front-End!'

@app.route('/search', methods=['GET'])
def search():
    user_input = request.args.get('query')
    conn = get_db_connection()
    cursor = conn.cursor()
    # Vulnerable SQL query
    try:
        result = cursor.execute(f"SELECT * FROM data WHERE info LIKE '%{user_input}%'").fetchall()
        conn.close()
        return jsonify([dict(ix) for ix in result])
    except Exception as e:
        conn.close()
        return str(e), 500

if __name__ == "__main__":
    init_db()  # Initialize the database and table
    app.run(host='0.0.0.0', port=5000)
