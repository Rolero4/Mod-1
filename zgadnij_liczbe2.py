from tkinter import *
from random import seed
from random import randint
import time
import sys
import os

def errorNumber():
    Błąd= Label(root, text= "Błąd. Podaj poprawną liczbę.")
    Błąd.grid(row=3, column=0)

def score_time(timeStop, timeStart):
    global timeDifference
    timeDifference = round(1000 * (timeStop - timeStart))
    if timeDifference <= 1000000:
        return 1000000 - timeDifference
    else:
        return 1
    return timeDifference

def submit():
    user_button.destroy()
    if ' ' in username.get():
        error= Label(root, text= "Błędna nazwa użytkownika")
        error.grid(row=8, column=0)
    else:
        fresults = open("wyniki.txt", "a")
        if fresults:
            fresults.write(username.get() + ", " + str(score) + "\n")
            fresults.close()
            name_alert= Label(root, text= "Wynik został zapisany", bg = 'light green')
            name_alert.grid(row=9, column=0)
        else:
            error_1= Label(root, text= "Błąd otwarcia pliku")
            error_1.grid(row=9, column=0)
    bye()

def save():    
    global username
    u_n = Label(root, text="Wpisz nazwe uzytkownika")
    u_n.grid(row=7, column=0)
    user_no.destroy()
    user_yes.destroy()
    username = Entry(root) 
    username.grid(row = 8, column = 0, padx=10)
    global user_button
    user_button = Button(root, text = "Zapisz", bg= 'light blue', command = submit)
    user_button.grid(row = 8, column = 1)

def bye():
    user_no.destroy()
    user_yes.destroy()
    thx = Label(root, text = "Dziękujemy za grę :)" , bg= 'light blue')
    thx.grid(row = 10 , column = 0)
    authors = Label(root, text="Kamil Giziński\nBartosz Rolnik\nDominik Sigulski")
    authors.grid(row=11, column = 0)

def check():

    guess=int(entry.get())
    text_alert = ' '

    if guess >= 1 and guess <= 100:
        if guess != randomInteger:
            if guess < randomInteger:
                text_alert ="za mała liczba\n"
            else:
                text_alert = "za duża liczba\n"
            info = Label(root, text = text_alert)
            info.grid(row=3, column=0)
        else:
            alert.destroy()
            entry.destroy()
            check_button.destroy()

            info = Label(root, text="Brawo, mój przyjacielu\n" , width = 20 , bg='light green')
            info.grid(row= 1, column=0)
            
            timeStop = time.perf_counter()

            global score
            score = score_time(timeStop, timeStart)
            score_label = Label(root, text= "Twoj wynik to: " + str(score) + "\n Chcesz zapisać wynik?")
            score_label.grid(row=3, column=0)

            global user_no
            global user_yes
            user_yes = Button(root, text = "TAK", bg= 'light blue', activebackground= 'blue', height = 1, width = 4, command = save)
            user_yes.grid(row = 4, column = 0)
            user_no = Button(root, text = "NIE", bg= 'light blue', activebackground= 'blue' , height = 1, width = 4, command = bye)
            user_no.grid(row = 4, column = 1)

    else:
        errorNumber()

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

root = Tk()
root.geometry('270x300')
root.title('Guess the number- the game')

mainMenu= Menu()
mainMenu.add_command(label= 'Scoreboard', command = show_scoreboard)

root.config(menu= mainMenu)

alert = Label(root, text= "Wpisz liczbe od 1 do 100")
alert.grid(row=0, column=0)

randomInteger = randint(1, 100)

timeStart = time.perf_counter()

entry = Entry(root)
entry.grid(row = 1, column = 0, padx=10)

check_button = Button(root, text = "Sprawdz", activebackground= 'blue', bg= 'light blue', command = check)
check_button.grid(row = 1, column = 1)

root.mainloop()

