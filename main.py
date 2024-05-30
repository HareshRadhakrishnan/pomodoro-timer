from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global rep
    rep =0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_lbl.config(text="Timer")
    Check_lbl.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():

    work_sec =WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec =LONG_BREAK_MIN*60
    global rep
    rep+=1
    if rep % 8 == 0:
        count_down(long_break_sec)
        title_lbl.config(text="Break", fg=RED)
    elif rep % 2 == 0:
            count_down(short_break_sec)
            title_lbl.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_lbl.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    min= floor(count/60)
    sec = count % 60

    if sec < 10:
        sec =f"0{sec}"


    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        timer = window.after(1000,count_down, count-1)
    else:
        start_timer()
        marks =""
        if rep % 2 ==0:
            marks+="✔"
            Check_lbl.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image = tomato_image)
timer_text = canvas.create_text(100,130,text="00:00", fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)

title_lbl = Label(text="Timer", font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW )
title_lbl.grid(row=1,column=2)
Start_btn = Button(text="Start", font=(FONT_NAME, 16, "bold") ,command=start_timer)
Start_btn .grid(row=3, column=1)
Reset_btn = Button(text="Reset", font=(FONT_NAME, 16, "bold"), command=reset_timer)
Reset_btn.grid(row=3, column=3)
Check_lbl = Label( font=(FONT_NAME,20,"bold"),fg=GREEN, bg =YELLOW)
Check_lbl .grid(row=4,column=2)
window.mainloop()