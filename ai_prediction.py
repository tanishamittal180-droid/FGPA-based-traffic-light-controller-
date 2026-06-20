import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Connect database

conn=sqlite3.connect("traffic.db")

query="""

SELECT cars,
pedestrians,
emergency

FROM traffic_data

"""

df=pd.read_sql(
query,
conn
)


if len(df)<5:

    print(
    "Not enough data collected."
    )

    exit()



# Features

X=df[
["pedestrians",
"emergency"]
]

# Target

y=df["cars"]


# Train model

model=LinearRegression()

model.fit(
X,
y
)


print("\nAI Traffic Predictor Ready\n")


while True:

    ped=int(input(
    "Pedestrians: "
    ))

    emergency=int(input(
    "Emergency (0/1): "
    ))


    prediction=model.predict(

    [[ped,emergency]]

    )


    traffic=max(
    0,
    int(prediction[0])
    )


    print(
    "\nPredicted Cars:",
    traffic
    )


    if traffic>30:

        print(
        "Heavy Traffic → Extend Green Time"
        )

    elif traffic>15:

        print(
        "Moderate Traffic"
        )

    else:

        print(
        "Low Traffic"
        )