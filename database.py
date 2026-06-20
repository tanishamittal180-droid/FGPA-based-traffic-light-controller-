import sqlite3
from datetime import datetime


conn=sqlite3.connect(
"traffic.db"
)

cur=conn.cursor()


cur.execute("""

CREATE TABLE IF NOT EXISTS traffic_data(

id INTEGER PRIMARY KEY AUTOINCREMENT,

timestamp TEXT,

cars INTEGER,

pedestrians INTEGER,

emergency INTEGER

)

""")


def save_data(

cars,
pedestrians,
emergency

):

    time=str(
    datetime.now()
    )

    cur.execute(

    '''

    INSERT INTO traffic_data(

    timestamp,
    cars,
    pedestrians,
    emergency

    )

    VALUES(?,?,?,?)

    ''',

    (

    time,
    cars,
    pedestrians,
    emergency

    )

    )

    conn.commit()