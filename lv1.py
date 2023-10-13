# TS.py

import sqlite3
from datetime import datetime
import random
import time

conn = sqlite3.connect('1020.db')

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS table1(ID integer,Current_time text,Amp integer)")

"""
cursor.execute("INSERT INTO table1 VALUES (0, '2022-10-19 20:53:00', 1)")
cursor.execute("INSERT INTO table1 VALUES (2, '2022-10-19 21:54:00', 2)")
cursor.execute("INSERT INTO table1 VALUES (3, '2022-10-19 22:55:00', 3)")
cursor.execute("INSERT INTO table1 VALUES (4, '2022-10-19 23:55:00', 4)")
cursor.execute("INSERT INTO table1 VALUES (5, '2022-10-19 24:55:00', 8)")
"""

N = 100;
Last_row = 0;


def Insert_Data(Current_time, Amp):
    if isFull():
        # print("Delete First")
        Delete_First()
        cursor.execute("INSERT INTO table1 VALUES (?, ?, ?)", ((Count_row() + Last_row) % N, Current_time, Amp))
    
    
    else:
        cursor.execute("INSERT INTO table1 VALUES (?, ?, ?)", ((Count_row() + Last_row) % N, Current_time, Amp))


def Print_all():
    for row in cursor.execute('SELECT * FROM table1'):
        print(row)


def Count_row():
    Count = 0
    for row in cursor.execute('SELECT * FROM table1'):
        Count = Count + 1
    return Count


def isFull():
    if Count_row() < N:
        return 0
    else:
        return 1


def Delete_First():
    global Last_row
    # print(Last_row)
    cursor.execute("DELETE FROM table1 WHERE ID = ?", ((Last_row,)))
    Last_row = (Last_row + 1) % N


Print_all()
start = time.time()

for i in range(10000):
    if i == 10:
        Print_all()
    Insert_Data(datetime.now(), random.randint(0, 1000))

end = time.time()
print(f"소요 시간 : {end - start:.4f}s")
Print_all()