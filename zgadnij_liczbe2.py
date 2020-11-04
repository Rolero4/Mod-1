from tkinter import *
from random import randint
import time
import sys
import os

highest = 100
lowest = 1
w = 0

def play():
    global alert
    alert = Label(root, text = "Wpisz liczbe od 1 do 100", width = 30, bg = "light blue")
    alert.grid(row = 0, column = 0, padx = 10)

    global randomInteger
    randomInteger = randint(1, 100)

    global p
    p = 1

    global timeStart
    timeStart = time.perf_counter()

    global entry
    entry = Entry(root)
    entry.grid(row = 1, column = 0, padx = 10, pady = 5)

    root.bind('<Return>', check)

def score_time(timeStop, timeStart):
    timeDifference = round(1000 * (timeStop - timeStart))
    if timeDifference <= 1000000:
        return 1000000 - timeDifference
    else:
        return 1

def submit():
    global name_alert

    while ' ' in username.get():
        error = Label(root, text= "Błędna nazwa użytkownika", width = 30)
        error.grid(row = 7, column = 0, padx = 10)
    else:
        fresults = open("wyniki.txt", "a")
        if fresults:
            fresults.write(username.get() + ", " + str(score) + "\n")
            fresults.close()
            name_alert = Label(root, text= "Wynik został zapisany", width = 30, bg = 'light green')
            name_alert.grid(row = 8, column = 0, padx = 10)
        else:
            error_1= Label(root, text= "Błąd otwarcia pliku", width = 30)
            error_1.grid(row= 7, column=0, padx=10)
    bye()

def save():    
    global username
    global u_n
    u_n = Label(root, text="Wpisz nazwe uzytkownika", width = 30)
    u_n.grid(row = 6, column = 0, padx = 10)
    user_no.destroy()
    user_yes.destroy()
    username = Entry(root) 
    username.grid(row = 7, column = 0, padx = 10)
    global user_button
    global w
    w = 1
    user_button = Button(root, text = "Zapisz", bg= 'light blue', command = submit)
    user_button.grid(row = 8, column = 0)

def bye():
    global w, thx, authors, restart_button
    score_label.destroy()
    info.destroy()
    user_no.destroy()
    user_yes.destroy()

    if w == 1:
        user_button.destroy()
        username.destroy()
        u_n.destroy()
        name_alert.destroy()

    thx = Label(root, text = "Dziękujemy za grę :)" , bg= 'light blue', width = 30)
    thx.grid(row = 0 , column = 0, padx = 10)
    
    authors = Label(root, text="Kamil Giziński\nBartosz Rolnik\nDominik Sigulski", width = 30)
    authors.grid(row = 1, column = 0)
    
    restart_button = Button(root, text = "RESTART", bg= 'light blue', activebackground = 'blue', height = 1, width = 30, command = restart)
    restart_button.grid(row = 2, column = 0, padx = 10)

def check(event):

    global info, h_o_l, lowest, highest, alert, score, score_label, user_yes, user_no

    try:
        guess = int(entry.get())
    except ValueError:

        text_alert = "Błąd. Podaj poprawną liczbę."
        info_error = Label(root, text = text_alert, bg = 'light grey')
        info_error.grid(row = 3, column = 0, padx = 20, pady = 1)
        entry.delete(0, END)

    else:
        text_alert = ''
        info = Label(root, text = text_alert, width = 24, height = 3)
        info.grid(row = 2, column = 0)
        info.destroy()
        if h_o_l == 1:
                highest = 100
                lowest = 1
                h_o_l = 2
        if guess >= lowest and guess <= highest:

            if guess != randomInteger:
                if guess < randomInteger:
                    text_alert = "Liczba " + entry.get() + " jest za mała"
                    lowest = guess + 1
                elif guess > randomInteger:
                    text_alert = "Liczba " + entry.get() + " jest za duża"
                    highest = guess - 1

                info = Label(root, text = text_alert, bg = 'light grey')
                info.grid(row = 2, column = 0, padx = 20)
                alert = Label(root, text= "Wpisz liczbę od " + str(lowest) + " do " + str(highest), width = 30, bg = "light blue")
                alert.grid(row = 0, column = 0, padx = 10)
                entry.delete(0, END)
    
            else:
                timeStop = time.perf_counter()
                alert.destroy()
                entry.destroy()
    
                info = Label(root, text = "Brawo, mój przyjacielu\n", width = 30 , height = 2,  bg = 'light green')
                info.grid(row = 0, column = 0, padx = 20, pady = 1)
                
                score = score_time(timeStop, timeStart)
    
                score_label = Label(root, text = "Twój wynik to: " + str(score) + "\n Chcesz zapisać wynik?", width = 30 )
                score_label.grid(row = 2, column=0, padx = 20, pady = 1)
    
                user_yes = Button(root, text = "TAK", bg= 'light blue', activebackground= 'blue', height = 1, width = 4, command = save)
                user_yes.grid(row = 4, column = 0)
                user_no = Button(root, text = "NIE", bg= 'light blue', activebackground= 'blue' , height = 1, width = 4, command = bye)
                user_no.grid(row = 5, column = 0)
    
        else:
            text_alert = "Błąd. Podaj liczbę od " + str(lowest) + " do " + str(highest)
            info = Label(root, text = text_alert, bg = 'light grey')
            info.grid(row = 2, column = 0, padx = 20, pady = 1)
            entry.delete(0, END)
        
def scores():
    score_root = Tk()
    score_root.geometry('270x500')
    score_root.title('Scoreboard')

    try:
        with open('wyniki.txt') as f_obj:
            players = f_obj.readlines()
    except FileNotFoundError:
        error = Label(score_root, text = "Przepraszamy, ale plik " + filename + " nie istnieje.")
        error.grid(row = 0, column = 0)
    else:
        results = []
        for player in players:
            i = 0
            while i < (len(player) - 1):
                if player[i] == ' ':
                    i += 1
                    results.append(player[i:len(player)])
                i += 1
        i = 0
        l = len(results)
        while i < l - 1:
            j=0
            while j < l - 1:
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
            label = Label(score_root, text = "Tabela wyników:\n")
            label.grid(row = 0, column = 0)
            i = 1
            l = len(players)
            while i < l:
                player = Label(score_root, text=str(i)+". " + str(players[i-1]))
                player.grid(row = i, column = 0)
                if i == 10:
                    break
                i += 1

def restart():
    global h_o_l, alert, info, randomInteger, timeStart, entry
    authors.destroy()
    thx.destroy()
    restart_button.destroy()
    score_label.destroy

    h_o_l = 1
    
    alert = Label(root, text = "Wpisz liczbe od 1 do 100", width = 30, bg = "light blue")
    alert.grid(row = 0, column = 0)
    info = Label(root, text = " ", width = 30, bg = "light grey")
    info.grid(row = 2, column = 0)


    randomInteger = randint(1, 100)

    timeStart = time.perf_counter()

    entry = Entry(root)
    entry.grid(row = 1, column = 0, padx = 10, pady = 5)

    root.bind('<Return>', check)

root = Tk()
root.geometry('270x500')
root.title('Guess the number - the game')

h_o_l = 1 

mainMenu= Menu()
 
mainMenu.add_command(label = 'Graj', command = play)  
mainMenu.add_command(label = 'Scoreboard', command = scores)   

root.config(menu = mainMenu)

root.mainloop()