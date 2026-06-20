import tkinter as tk
from tkinter import ttk
import random
from database import save_data

root = tk.Tk()

root.title("AI Smart Traffic Management System")
root.geometry("1450x850")
root.configure(bg="#111111")

# ===========================
# VARIABLES
# ===========================

emergency=False
pedestrian=False

cars_passed=0
ped_count=0
emergency_count=0

phase=0


# ===========================
# MAIN CANVAS
# ===========================

canvas=tk.Canvas(
    root,
    width=1000,
    height=850,
    bg="#1a1a1a",
    highlightthickness=0
)

canvas.pack(side="left")


# ===========================
# ROADS
# ===========================

canvas.create_rectangle(
    0,350,1000,500,
    fill="#444"
)

canvas.create_rectangle(
    425,0,575,850,
    fill="#444"
)


# Road markings

for i in range(0,1000,60):

    canvas.create_rectangle(
        i,
        420,
        i+25,
        430,
        fill="white"
    )


for i in range(0,850,60):

    canvas.create_rectangle(
        495,
        i,
        505,
        i+25,
        fill="white"
    )


canvas.create_text(
    500,
    30,
    text="SMART TRAFFIC MANAGEMENT SYSTEM",
    font=("Arial",20,"bold"),
    fill="white"
)



# ===========================
# SIGNALS
# ===========================

def create_signal(x,y):

    canvas.create_rectangle(
        x,
        y,
        x+70,
        y+180,
        fill="black"
    )

    r=canvas.create_oval(
        x+15,
        y+15,
        x+55,
        y+55,
        fill="gray"
    )

    y1=canvas.create_oval(
        x+15,
        y+70,
        x+55,
        y+110,
        fill="gray"
    )

    g=canvas.create_oval(
        x+15,
        y+125,
        x+55,
        y+165,
        fill="gray"
    )

    return r,y1,g



ns_r,ns_y,ns_g=create_signal(
    280,
    90
)

ew_r,ew_y,ew_g=create_signal(
    650,
    90
)



# ===========================
# CARS
# ===========================

horizontal=[]
vertical=[]


for i in range(7):

    car=canvas.create_rectangle(

        random.randint(0,900),

        random.choice([380,460]),

        random.randint(50,950),

        random.choice([410,490]),

        fill=random.choice(
            [
                "red",
                "blue",
                "yellow",
                "orange",
                "cyan",
                "purple"
            ]
        )
    )

    horizontal.append(car)



for i in range(7):

    car=canvas.create_rectangle(

        random.choice([450,520]),

        random.randint(0,800),

        random.choice([480,550]),

        random.randint(50,850),

        fill=random.choice(
            [
                "green",
                "pink",
                "white"
            ]
        )
    )

    vertical.append(car)



# ===========================
# CONTROL PANEL
# ===========================

panel=tk.Frame(
    root,
    bg="#222",
    width=400
)

panel.pack(
    side="right",
    fill="y"
)


title=tk.Label(
panel,
text="CONTROL PANEL",
font=("Arial",18,"bold"),
bg="#222",
fg="white"
)

title.pack(pady=20)



# ===========================
# BUTTONS
# ===========================

def emergency_toggle():

    global emergency
    global emergency_count

    emergency=not emergency

    if emergency:

        emergency_count+=1



def pedestrian_toggle():

    global pedestrian
    global ped_count

    pedestrian=not pedestrian

    if pedestrian:

        ped_count+=1



tk.Button(
panel,
text="Emergency",
command=emergency_toggle,
bg="red",
width=20
).pack(pady=10)


tk.Button(
panel,
text="Pedestrian",
command=pedestrian_toggle,
bg="lightblue",
width=20
).pack(pady=10)



# ===========================
# DENSITY SLIDER
# ===========================

tk.Label(
panel,
text="Traffic Density",
bg="#222",
fg="white"
).pack()

density=ttk.Scale(
panel,
from_=1,
to=20,
orient="horizontal"
)

density.pack()



# ===========================
# STATUS LABELS
# ===========================

status=tk.Label(
panel,
text="Status",
font=("Arial",14),
bg="#222",
fg="white"
)

status.pack(pady=20)



prediction=tk.Label(
panel,
text="AI Prediction",
font=("Arial",14),
bg="#222",
fg="cyan"
)

prediction.pack()



stats=tk.Label(
panel,
text="",
font=("Arial",12),
bg="#222",
fg="white"
)

stats.pack(
pady=20
)



# ===========================
# UPDATE FUNCTION
# ===========================

def update():

    global phase
    global cars_passed

    lights=[

        ns_r,
        ns_y,
        ns_g,

        ew_r,
        ew_y,
        ew_g
    ]


    for l in lights:

        canvas.itemconfig(
            l,
            fill="gray"
        )


    if emergency:

        canvas.itemconfig(
            ns_g,
            fill="green"
        )

        canvas.itemconfig(
            ew_r,
            fill="red"
        )

        current="EMERGENCY MODE"


    else:

        if phase==0:

            canvas.itemconfig(
                ns_g,
                fill="green"
            )

            canvas.itemconfig(
                ew_r,
                fill="red"
            )

            current="NS GREEN"


        elif phase==1:

            canvas.itemconfig(
                ns_y,
                fill="yellow"
            )

            current="NS YELLOW"


        elif phase==2:

            canvas.itemconfig(
                ew_g,
                fill="green"
            )

            canvas.itemconfig(
                ns_r,
                fill="red"
            )

            current="EW GREEN"


        else:

            canvas.itemconfig(
                ew_y,
                fill="yellow"
            )

            current="EW YELLOW"


        phase=(phase+1)%4


    speed=int(
        density.get()
    )


    for car in horizontal:

        canvas.move(
            car,
            speed,
            0
        )

        pos=canvas.coords(car)

        if pos[0]>1000:

            canvas.move(
                car,
                -1100,
                0
            )

            cars_passed+=1


    for car in vertical:

        canvas.move(
            car,
            0,
            speed
        )

        pos=canvas.coords(car)

        if pos[1]>850:

            canvas.move(
                car,
                0,
                -900
            )

            cars_passed+=1


    traffic=random.randint(
        1,
        100
    )


    if traffic>70:

        ai_text="Heavy Traffic"

    elif traffic>30:

        ai_text="Moderate Traffic"

    else:

        ai_text="Low Traffic"



    prediction.config(
        text=f"AI Prediction : {ai_text}"
    )


    status.config(
        text=f"Current State : {current}"
    )


    stats.config(

text=f"""

Cars Passed : {cars_passed}

Pedestrians : {ped_count}

Emergency : {emergency_count}

Density : {speed}

"""
)


    save_data(
        cars_passed,
        ped_count,
        emergency_count
    )


    root.after(
        2000,
        update
    )


update()

root.mainloop()