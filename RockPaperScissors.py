from tkinter import *
import random

root=Tk()
root.geometry('400x400')
root.title('Rock,  Paper, Scissor Game')
root.config(bg='black')

Label(root,text='Rock, Paper, Scissors',font='Georgia 20 bold',fg='white',bg='black').pack()
user=StringVar()
Label(root,text='Choose any one : rock, paper, scissors',font='Georgia 13 bold',fg='white',bg='black').place(x=20,y=70)
Entry(root,font='Gerogia 15',textvariable=user,bg='antiquewhite2').place(x=90,y=130)

res=StringVar()
def play():
    user_choice=user.get()
    comp=random.randint(1,3)
    if comp==1:
        comp='rock'
    elif comp==2:
        comp='paper'
    else:
        comp='scissors'
    if user_choice==comp:
        res.set("It's a tie!")
    elif user_choice=='rock' and comp=='paper':
        res.set("You lose! Computer chose paper")
    elif user_choice=='rock' and comp=='scissors':
        res.set("You win! Computer chose scissors")
    elif user_choice=='paper' and comp=='rock':
        res.set("You win! Computer chose rock")
    elif user_choice=='paper' and comp=='scissors':
        res.set("You lose! Computer chose scissors")
    elif user_choice=='scissors' and comp=='rock':
        res.set("You lose! Computer chose rock")
    elif user_choice=='scissors' and comp=='paper':
        res.set("You win! Computer chose paper")
    else:
        res.set("Invalid: choose any one-- rock,paper,scissors")

def reset():
    res.set('')
    user.set('')
def Exit():
    root.destroy()

Entry(root, font = 'Gerogia 12 bold', textvariable = res, bg ='antiquewhite2',width = 40,).place(x=20, y = 250)
Button(root, font = 'Gerogia 13 bold', text = 'PLAY'  ,padx =5,bg ='#55ff00' ,command = play).place(x=150,y=190)
Button(root, font = 'Gerogia 13 bold', text = 'RESET'  ,padx =5,bg ='#49A' ,command = reset).place(x=70,y=310)
Button(root, font = 'Gerogia 13 bold', text = 'EXIT'  ,padx =5,bg ='#ff1a1a' ,command = Exit).place(x=230,y=310)

root.mainloop()
