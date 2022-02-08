from tkinter import *
import requests
import random


my_file = open("movies.txt", "r")

data= my_file.read()
data_into_list = data.split("\n")

watched = []

def movie_picker():

    global watched

    movie_of_the_day = random.choice(data_into_list)
    output.config(text = f"{movie_of_the_day}")
    if movie_of_the_day in watched:
        label2.config(text="You have already watched this movie.")
    else:
        label2.config(text="Enjoy your movie!")
    watched.append(movie_of_the_day)

    with open("watched.txt", mode="w") as file:
        for movie in watched:
            file.write(f"{movie_of_the_day}")






screen = Tk()
screen.geometry("250x180")
screen.config(pady=20, padx=20)

label = Label(text="The movie of the day...")
label.grid(column=0, row=0)

label2 = Label(text="",)
label2.grid(column=0, row=5)

button = Button(text="Pick a movie",bg="coral" ,command=movie_picker)
button.grid(column=0, row=1)

output = Label(text="")
output.grid(column=0, row=2)


screen.mainloop()





