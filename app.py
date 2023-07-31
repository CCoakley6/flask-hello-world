import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab9postgresql_user:T7yhE4Qqxfpy6ElaKkyUnMV1hXGmoKpf@dpg-cj3g0qd9aq0e0q76mht0-a/lab9postgresql")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def create():
    conn = psycopg2.connect("postgres://lab9postgresql_user:T7yhE4Qqxfpy6ElaKkyUnMV1hXGmoKpf@dpg-cj3g0qd9aq0e0q76mht0-a/lab9postgresql")
    cur = conn.cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.commit()
    
    conn.close()
    return "Basketball table was successfully created."