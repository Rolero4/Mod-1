from tkinter import *
from random import seed
from random import randint
import time
import sys
import os

global highest 
highest = 100
global lowest 
lowest = 1

def play():
    global alert
    alert = Label(root, text= "Wpisz liczbe od 1 do 100", width = 37, bg= "light blue")
    alert.grid(row=0, column=0)


    global randomInteger
    randomInteger = randint(1, 100)

    global p
    p=1

    global timeStart
    timeStart = time.perf_counter()

    global entry
    entry = Entry(root)
    entry.grid(row = 1, column = 0, padx=10, pady = 5)

    root.bind('<Return>', check)

def score_time(timeStop, timeStart):
    timeDifference = round(1000 * (timeStop - timeStart))
    if timeDifference <= 1000000:
        return 1000000 - timeDifference
    else:
        return 1
    return timeDifference

def submit():
    user_button.destroy()
    if ' ' in username.get():
        error= Label(root, text= "Błędna nazwa użytkownika", width = 37)
        error.grid(row=7, column=0)
    else:
        fresults = open("wyniki.txt", "a")
        if fresults:
            fresults.write(username.get() + ", " + str(score) + "\n")
            fresults.close()
            name_alert= Label(root, text= "Wynik został zapisany", width = 37, bg = 'light green')
            name_alert.grid(row= 8, column=0)
        else:
            error_1= Label(root, text= "Błąd otwarcia pliku", width = 37)
            error_1.grid(row= 7, column=0)
    bye()

def save():    
    global username
    u_n = Label(root, text="Wpisz nazwe uzytkownika", width = 37)
    u_n.grid(row= 6, column=0)
    user_no.destroy()
    user_yes.destroy()
    username = Entry(root) 
    username.grid(row = 7, column = 0, padx=10)
    global user_button
    user_button = Button(root, text = "Zapisz", bg= 'light blue', command = submit)
    user_button.grid(row =7, column = 0)

def bye():
    info.destroy()
    user_no.destroy()
    user_yes.destroy()
    global thx
    thx = Label(root, text = "Dziękujemy za grę :)" , bg= 'light blue', width = 30)
    thx.grid(row = 9 , column = 0, pady = 5)
    global authors
    authors = Label(root, text="Kamil Giziński\nBartosz Rolnik\nDominik Sigulski", width = 30)
    authors.grid(row=10, column = 0)
    global restart_button
    restart_button= Button(root, text = "RESTART", bg= 'light blue', activebackground= 'blue', height = 1, width = 10, command = restart)
    restart_button.grid(row = 11, column = 0)

def check(event):

    global info 
    guess=int(entry.get())

    info = Label(root, text = " ", width = 24, height= 3)
    info.grid(row=2, column=0)
    info.destroy()
    text_alert = ' '

    if h_o_l == True:
        highest = 100
        lowest = 1
        h_o_l == False
        


    if guess >= 1 and guess <= 100:
        if guess != randomInteger:
            if guess < randomInteger >=lowest:
                text_alert = "Liczba " + entry.get()+ " jest za mała"
                lowest = guess +1
            elif guess > randomInteger <= highest:
                text_alert = "Liczba " + entry.get()+ " jest za duża"
                highest = guess - 1 

            info = Label(root, text = text_alert, bg = 'light grey')
            info.grid(row= 2, column=0, padx = 20, pady=1)
            alert = Label(root, text= "Wpisz liczbe od "+ str(lowest)+ " do "+str(highest), width = 37, bg= "light blue")
            alert.grid(row=0, column=0)

        else:
            alert.destroy()
            entry.destroy()

            info = Label(root, text="Brawo, mój przyjacielu\n" ,width = 30 , height = 2,  bg='light green')
            info.grid(row= 1, column=0, padx = 20, pady=1)
            
            timeStop = time.perf_counter()

            global score
            score = score_time(timeStop, timeStart)
            global score_label
            score_label = Label(root, text= "Twoj wynik to: " + str(score) + "\n Chcesz zapisać wynik?", )
            score_label.grid(row=2, column=0, padx = 20, pady=1)

            global user_no
            global user_yes
            user_yes = Button(root, text = "TAK", bg= 'light blue', activebackground= 'blue', height = 1, width = 4, command = save)
            user_yes.grid(row = 4, column = 0)
            user_no = Button(root, text = "NIE", bg= 'light blue', activebackground= 'blue' , height = 1, width = 4, command = bye)
            user_no.grid(row = 4, column = 0)

    else:
        text_alert= "Błąd. Podaj poprawną liczbę."
        info = Label(root, text = text_alert, bg = 'light grey')
        info.grid(row=2, column=0, padx = 20, pady=1)
        
    entry.delete(0,END)

def show_scoreboard():
    scores('wyniki.txt')

def scores(filename):
    score_root = Tk()
    score_root.geometry('270x500')
    score_root.title('Scoreboard')

    try:
        with open(filename) as f_obj:
            players = f_obj.readlines()
    except FileNotFoundError:
        error = Label(score_root, text="Przepraszamy, ale plik " + filename + "' nie istnieje.")
        error.grid(row=0, column=0)
    else:
        results = []
        for player in players:
            i = 0
            while i < (len(player)-1):
                if player[i] == ' ':
                    i += 1
                    results.append(player[i:len(player)])
                i += 1
        i = 0
        l = len(results)
        while i < l-1:
            j=0
            while j < l-1:
                if results[j] < results[j+1]:
                    tempResults = results[j+1]
                    tempPlayers = players[j+1]
                    results[j+1] = results[j]
                    players[j+1] = players[j]
                    results[j] = tempResults
                    players[j] = tempPlayers
                j += 1
            i += 1           
        if players:
            label = Label(score_root, text="Tabela wyników:\n")
            label.grid(row=0, column=0)
            i = 1
            l = len(players)
            while i < l:
                player = Label(score_root, text=str(i)+". " + str(players[i-1]))
                player.grid(row=i, column=0)
                if i == 10:
                    break
                i += 1

def restart():
    authors.destroy()
    thx.destroy()
    restart_button.destroy()
    score_label.destroy


    lowest = 100
    highest = 0


    global alert
    alert = Label(root, text= "Wpisz liczbe od 1 do 100", width = 37, bg= "light blue")
    alert.grid(row=0, column=0)

    global randomInteger
    randomInteger = randint(1, 100)

    global timeStart
    timeStart = time.perf_counter()

    global entry
    entry = Entry(root)
    entry.grid(row = 1, column = 0, padx=10, pady = 5)

    root.bind('<Return>', check)


root = Tk()
root.geometry('300x500')
root.title('Guess the number- the game')

h_o_l = True 

mainMenu= Menu()
 
mainMenu.add_command(label= 'Graj', command = play)  
mainMenu.add_command(label= 'Scoreboard', command = show_scoreboard)   

root.config(menu= mainMenu)


root.mainloop()

