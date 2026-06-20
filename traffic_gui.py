import tkinter as tk

root = tk.Tk()

root.title("Smart Traffic Light Controller")
root.geometry("900x650")

canvas=tk.Canvas(root,width=900,height=650,bg="lightgreen")
canvas.pack()

# Roads
canvas.create_rectangle(0,250,900,400,fill="gray")
canvas.create_rectangle(350,0,550,650,fill="gray")

# Road markings
for i in range(0,900,50):
    canvas.create_rectangle(i,320,i+25,330,fill="white")

for i in range(0,650,50):
    canvas.create_rectangle(445,i,455,i+25,fill="white")


canvas.create_text(
450,
30,
text="Smart Traffic Controller",
font=("Arial",20,"bold")
)

# NS lights box
canvas.create_rectangle(
150,
100,
250,
260,
fill="black"
)

# EW lights box
canvas.create_rectangle(
650,
100,
750,
260,
fill="black"
)


# NS traffic lights

ns_red=canvas.create_oval(
180,120,220,160,
fill="gray"
)

ns_yellow=canvas.create_oval(
180,170,220,210,
fill="gray"
)

ns_green=canvas.create_oval(
180,220,220,260,
fill="gray"
)


# EW traffic lights

ew_red=canvas.create_oval(
680,120,720,160,
fill="gray"
)

ew_yellow=canvas.create_oval(
680,170,720,210,
fill="gray"
)

ew_green=canvas.create_oval(
680,220,720,260,
fill="gray"
)


# Cars

car1=canvas.create_rectangle(
0,280,50,320,
fill="blue"
)

car2=canvas.create_rectangle(
850,350,900,390,
fill="red"
)

car3=canvas.create_rectangle(
390,0,430,50,
fill="yellow"
)

car4=canvas.create_rectangle(
480,600,520,650,
fill="purple"
)

count_label=canvas.create_text(
450,
600,
text="",
font=("Arial",18)
)

state=0
counter=5


def move_cars():

    global state

    if state==0:

        canvas.move(car1,10,0)
        canvas.move(car2,-10,0)

    elif state==2:

        canvas.move(car3,0,10)
        canvas.move(car4,0,-10)



def update():

    global state
    global counter

    lights=[

    ns_red,
    ns_yellow,
    ns_green,
    ew_red,
    ew_yellow,
    ew_green

    ]


    for x in lights:

        canvas.itemconfig(
        x,
        fill="gray"
        )


    if state==0:

        canvas.itemconfig(
        ns_green,
        fill="green"
        )

        canvas.itemconfig(
        ew_red,
        fill="red"
        )

        canvas.itemconfig(
        count_label,
        text="NS Green : 5 sec"
        )


    elif state==1:

        canvas.itemconfig(
        ns_yellow,
        fill="yellow"
        )

        canvas.itemconfig(
        ew_red,
        fill="red"
        )

        canvas.itemconfig(
        count_label,
        text="NS Yellow : 2 sec"
        )


    elif state==2:

        canvas.itemconfig(
        ns_red,
        fill="red"
        )

        canvas.itemconfig(
        ew_green,
        fill="green"
        )

        canvas.itemconfig(
        count_label,
        text="EW Green : 5 sec"
        )


    elif state==3:

        canvas.itemconfig(
        ns_red,
        fill="red"
        )

        canvas.itemconfig(
        ew_yellow,
        fill="yellow"
        )

        canvas.itemconfig(
        count_label,
        text="EW Yellow : 2 sec"
        )


    move_cars()

    state=(state+1)%4


    if state==0 or state==2:

        root.after(
        5000,
        update
        )

    else:

        root.after(
        2000,
        update
        )


update()

root.mainloop()