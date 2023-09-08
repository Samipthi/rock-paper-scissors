'''
from  tkinter import *
import random
from PIL import ImageTk,Image
'''
import random
import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("ROCK PAPER SCISSORS ")

root.geometry('800x680')

canvas=Canvas(root, width=800, height=680)
canvas.grid(row=0, column=0)
canvas.configure(bg='black')
l1 = Label(root, text='Player', font=('Times', 25),background="black",foreground="white")
l2 = Label(root, text='Computer', font=('Times', 25),background="black",foreground="white")
l3 = Label(root, text='Vs', font=('Times', 40),background="black",foreground="white")

l1.place(x=80, y=20)
l2.place(x=560, y=20)
l3.place(x=370, y=230)

img_p=Image.open("default.png")
img_p=img_p.resize((300,300))

img_p = ImageTk.PhotoImage(img_p)

rock_p = Image.open("rock.png")
rock_p= rock_p.resize((300,300))
rock_c = rock_p.transpose(Image.FLIP_LEFT_RIGHT)

rock_c= ImageTk.PhotoImage(rock_c)
rock_p= ImageTk.PhotoImage(rock_p)

paper_p = Image.open("paper.png")
paper_p= paper_p.resize((300,300))

paper_p= ImageTk.PhotoImage(paper_p)

scissor_p = Image.open("scissor.png")
scissor_p_p= scissor_p.resize((300,300))
scissor_c = scissor_p.transpose(Image.FLIP_LEFT_RIGHT)

scissor_c= ImageTk.PhotoImage(scissor_c)
scissor_p= ImageTk.PhotoImage(scissor_p)

def game(player):
    select=[1,2,3]

    computer=random.choice(select)
    if player==1:
        canvas.create_image(0, 100, anchor=NW, image=rock_p)
    elif player==2:
        canvas.create_image(0,100, anchor=NW, image=paper_p)
    elif player==3:
        canvas.create_image(0, 100, anchor=NW, image=scissor_p)

    if computer==1:
        canvas.create_image(500, 100, anchor=NW, image=rock_p)
    elif computer==2:
        canvas.create_image(500,100, anchor=NW, image=paper_p)
    elif computer==3:
        canvas.create_image(500, 100, anchor=NW, image=scissor_c)

    if player == computer:  # Case of DRAW
        res = 'Draw'

    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or(player == 3 and computer == 2):
        res = 'You won'

    else:
        res = 'Computer won'

    canvas.create_text( 390 , 550 ,text='Result:  ' + res ,fill="white" , font=('Times', 25) , tag='result' )

def clear():
    canvas.delete('result')

    canvas.create_image(0, 100, anchor=NW, image=img_p)
    canvas.create_image(500, 100, anchor=NW, image=img_p)


rock_b = Button(root, text='Rock', command=lambda: game(1),width=10,height=2)
rock_b.place(x=50, y=487)

# Button for selecting paper
paper_b = Button(root, text='Paper', command=lambda: game(2),width=10,height=2)
paper_b.place(x=350, y=487)

# Button for selecting scissor
scissor_b = Button(root, text='Scissor', command=lambda: game(3),width=10,height=2)
scissor_b.place(x=650, y=487)

# Button for clear
clear_b = Button(root, text='CLEAR', font=('Times', 10, 'bold'),
                 width=10, command=clear).place(x=350, y=600)


root.mainloop()

