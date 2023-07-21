from tkinter import *
from tkinter import PhotoImage

import pandas
from pandas import *
from random import choice, randint
new = None
BACKGROUND_COLOR = "#B1DDC6"
try:
    file_data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    file_data = read_excel("data/word_list.xlsx")
else:
    pass
finally:
    word_to_learn = file_data.to_dict(orient="records")
# ---------turn the card------
def turn_word():
    global new

    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=new["english"], fill="white")
# ---------generate a random word------

def new_word():
    global new, turn_timer
    window.after_cancel(turn_timer)
    canvas.itemconfig(canvas_image, image=card_front)
    new = choice(word_to_learn)
    new_sw_word = new["swedish"]
    canvas.itemconfig(word, text=new_sw_word, fill="black")
    canvas.itemconfig(title, text="Swedish", fill="black")
    turn_timer = canvas.after(3000, turn_word)

# --------------remove word-------------

def remove_word():
    global new
    word_to_learn.remove(new)
    new_word()
    data = pandas.DataFrame(word_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

# --------------making UI--------------

window = Tk()
window.title("Flash Cards For Swedish Word")
window.iconbitmap("./images/flashcards.ico")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
turn_timer = window.after(3000, turn_word)
canvas = Canvas(width=800, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
deny_image = PhotoImage(file='images/wrong.png')
deny_button = Button(width=100, height=100, image=deny_image, highlightthickness=0, bg=BACKGROUND_COLOR,
                     command=new_word)
deny_button.grid(column=0, row=1)
accept_image = PhotoImage(file="images/right.png")
accept_button = Button(width=100, height=100, image=accept_image, highlightthickness=0, bg=BACKGROUND_COLOR,
                       command=remove_word)
accept_button.grid(column=1, row=1)
title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
new_word()

window.mainloop()
