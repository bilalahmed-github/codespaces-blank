import psycopg2

def connect_db():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="mysecretpassword",
        host="mydatabase",
        port=5432
    )
    return conn

def create_table(conn):
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(255), age INT);")
    conn.commit()
    cur.close()

def insert_user(conn, name, age):
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s) RETURNING id;", (name, age))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    return user_id

def get_all_users(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, name, age FROM users;")
    users = [{"id": row[0], "name": row[1], "age": row[2]} for row in cur.fetchall()]
    cur.close()
    return users
