from tkinter import *
import random

def next_turn(row,coloumn):
    global player

    if buttons[row][coloumn]['text'] == "" and check_winner() is False:
        
        if player == players[0]:
            buttons[row][coloumn]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=("<<<< "+players[1]+" turn >>>>"))
            elif check_winner() is True:
                label.config(text=("-----"+players[0]+" Wins-----"))  
            elif check_winner() == "Tie":
                label.config(text=("-----Tie-----"))
        
        else:
            buttons[row][coloumn]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=("<<<< " + players[0]+" turn >>>>"))
            elif check_winner() is True:
                label.config(text=("-----"+players[1]+" Wins-----"))  
            elif check_winner() == "Tie":
                label.config(text=("-----Tie-----"))



def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg = "green")
            buttons[row][1].config(bg = "green")
            buttons[row][2].config(bg = "green")
            return True
    for coloumn in range(3):
        if buttons[0][coloumn]['text'] == buttons[1][coloumn]['text'] == buttons[2][coloumn]['text'] != "":
            buttons[0][coloumn].config(bg = "green")
            buttons[1][coloumn].config(bg = "green")
            buttons[2][coloumn].config(bg = "green")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":    
        buttons[0][0].config(bg = "green")
        buttons[1][1].config(bg = "green")
        buttons[2][2].config(bg = "green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "": 
        buttons[0][2].config(bg = "green")
        buttons[1][1].config(bg = "green")
        buttons[2][0].config(bg = "green")   
        return True
    elif empty_spaces() is False:
            for row in range(3):
                for coloumn in range(3):
                    buttons[row][coloumn].config(bg ="yellow")
            return "Tie"
    else:
        return False

def empty_spaces():
    spaces = 9

    for row in range(3):
       for coloumn in range(3):
           if buttons[row][coloumn]['text'] != "":
               spaces -= 1

    if spaces == 0:
        return False
    else:
        return True           
             

    
def new_game():
    
    global player

    player = random.choice(players)

    label.config(text ="<<<< " + player + " Turn >>>>")

    for row in range(3):
         for coloumn in range(3):
             buttons[row][coloumn].config(text="",bg="pink")


window = Tk()
window.title("Tic-Tac-Toe")
players = ["B","S"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
label = Label(text ="<<<< " + player + " Turn >>>>",font=('consolas',40) )
label.pack(side = "top")

reset_button = Button(text= "<---Restart--->",bg="skyblue",font = ('consolas',20),command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for coloumn in range(3):
        buttons[row][coloumn] = Button(frame,text="",font=('consolas',40),width = 5,height =2,bg="pink" ,command= lambda row=row,coloumn=coloumn :next_turn(row,coloumn))
        buttons[row][coloumn].grid(row=row,column=coloumn)

window.mainloop()