import sqlite3
username = 'admin'
password = 'admin'
PATH = r'C:\Users\Acer\OneDrive\Desktop\sms1\database.db'
def connect():
    conn = sqlite3.connect(PATH)
    return conn
def create_table_student():
    conn=connect()
    c=conn.cursor()
    c.execute('''create table student(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT,
                Roll_num TEXT,
                Fname TEXT,
                Gender TEXT,
                Branch TEXT,
                Contact TEXT,
                Address TEXT
                
                )''')
    conn.commit()
    conn.close()



create_table_student()

