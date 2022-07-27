import time
from datetime import datetime
from tkinter import *

# helv36 = Tk.tkFont.Font(family='Helvetica',size=36, weight='bold')


def updateTime():
    global Curr_Hr, Curr_Min, Curr_Sec
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    Curr_Hr = int(now.strftime("%H"))%12
    Curr_Min = int(now.strftime("%M"))
    Curr_Sec = int(now.strftime("%S"))
    # print("Current Time =", current_time)


def clear():
    can.delete("all")

# Roboto 20 italic bold

def ArcUpdate():
    updateTime()
    clear()
    TMinText = can.create_text(80, 500, text=Curr_Hr,font="Roboto 20 bold")
    TextC1 = can.create_text(160, 500, text=":",font="Roboto 20 bold")
    THrText = can.create_text(240, 500, text=Curr_Min,font="Roboto 20 bold")
    Textc2 = can.create_text(320, 500, text=":",font="Roboto 20 bold")
    TSecText = can.create_text(400, 500, text=Curr_Sec,font="Roboto 20 bold")

    CreateSecArc = can.create_arc((50, 50, 450, 450), start=-270, extent=-(Curr_Sec * 6), style='arc',dash=(3, 1, 2, 1),width=10,outline="blue")

    CreateMinArc = can.create_arc((80, 80, 420, 420), start=-270, extent=-(Curr_Min * 6), style='arc',width=5,outline="maroon")

    CreateHeArc = can.create_arc((100, 100, 400, 400), start=-270, extent=-(Curr_Hr * 30), style='arc',width=3,outline="white")

    can.pack()
    # print(Curr_Sec)
    can.after(1000, ArcUpdate)


# Draw a curve
win = Tk()
win.geometry("500x600")

global can
global coords
global r

r = 50

commonStart = 270

can = Canvas(win, bg="purple", height=600, width=500)

ArcUpdate()

can.pack()

# win.after(4000,clear)


win.mainloop()
