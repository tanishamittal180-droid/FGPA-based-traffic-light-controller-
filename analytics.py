import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Connect database
conn=sqlite3.connect("traffic.db")

fig,ax=plt.subplots()

def update(frame):

    ax.clear()

    query="""

    SELECT *
    FROM traffic_data

    """

    df=pd.read_sql(query,conn)

    if len(df)==0:
        return


    ax.plot(
    df["cars"],
    label="Cars Passed"
    )

    ax.plot(
    df["pedestrians"],
    label="Pedestrians"
    )

    ax.plot(
    df["emergency"],
    label="Emergency Events"
    )

    ax.set_title(
    "Smart Traffic Analytics"
    )

    ax.set_xlabel(
    "Time Index"
    )

    ax.set_ylabel(
    "Count"
    )

    ax.legend()


ani=FuncAnimation(

fig,
update,
interval=1000

)

plt.show()