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
def creating():
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


@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgres://lab9postgresql_user:T7yhE4Qqxfpy6ElaKkyUnMV1hXGmoKpf@dpg-cj3g0qd9aq0e0q76mht0-a/lab9postgresql")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball table was successfully created."

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgres://lab9postgresql_user:T7yhE4Qqxfpy6ElaKkyUnMV1hXGmoKpf@dpg-cj3g0qd9aq0e0q76mht0-a/lab9postgresql")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_string = ""
    response_string =+"<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    return response_string