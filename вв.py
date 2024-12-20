
from tkinter import *
from PIL import Image
import random
from time import *
import threading
import pygame
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

width = 1440
height = 900
score = 0
hole = 0
highscore = 0
countdown = 76

app.geometry(f"{width}x{height}")
# app.attributes('-fullscreen', True)
app.title("Whack A Squ")


# ALL THE FUNCTIONSSSSS


# when start button pressed, this will happen, determines the points
def start():
    menu.place_forget()
    htp.place_forget()
    background_music.play()
    global score
    score = 0
    score_label.configure(text=f"Score:{score}")
    playbtn.place_forget()
    playbtn.place_forget()
    kailesurugarne.place(x=570, y=130)
    t = threading.Thread(target=whac_a_mole)
    t.start()


def onwhack():
    global hole
    global score
    if hole == 1:
        trigger_sqrl1.configure(state='disabled', image=bonked)
    elif hole == 2:
        trigger_sqrl2.configure(state='disabled', image=bonked)
    elif hole == 3:
        trigger_sqrl3.configure(state='disabled', image=bonked)
    elif hole == 4:
        trigger_sqrl4.configure(state='disabled', image=bonked)
    elif hole == 5:
        trigger_sqrl5.configure(state='disabled', image=bonked)
    elif hole == 6:
        trigger_sqrl6.configure(state='disabled', image=bonked)
    elif hole == 7:
        trigger_sqrl7.configure(state='disabled', image=bonked)
    elif hole == 8:
        trigger_sqrl8.configure(state='disabled', image=bonked)

    score += 10
    score_label.configure(text=f"Score:{score}")


# this is the function for the game, this determines where the rats will spawn, and also when the game end
def whac_a_mole():
    ready_set_whack()
    county.place(x=540, y=130)
    global countdown
    countdown = 76
    global hole
    global score
    global highscore
    for i in range(0, 76):
        countdown -= 1
        county.configure(text=f"Rats Left:{countdown}")
        hole = random.randint(1, 8)
        if hole == 1:
            squirell_sound.play()
            trigger_sqrl1.configure(
                state='normal',
                image=squirell, )
            trigger_sqrl1.place(x=220, y=255)
            sleep(0.75)
            trigger_sqrl1.configure(state='disabled', )
            trigger_sqrl1.place_forget()
        elif hole == 2:
            squirell_sound.play()
            trigger_sqrl2.configure(
                state='normal',
                image=squirell, )
            trigger_sqrl2.place(x=620, y=260)
            sleep(0.75)
            trigger_sqrl2.configure(state='disabled', text='', )
            trigger_sqrl2.place_forget()
        elif hole == 3:
            squirell_sound.play()
            trigger_sqrl3.configure(
                state='normal',
                image=squirell, )
            trigger_sqrl3.place(x=1000, y=255)
            sleep(0.75)
            trigger_sqrl3.configure(state='disabled', text='', )
            trigger_sqrl3.place_forget()
        elif hole == 4:
            squirell_sound.play()
            trigger_sqrl4.configure(
                state='normal',
                image=squirell, )
            trigger_sqrl4.place(x=400, y=400)
            sleep(0.75)
            trigger_sqrl4.configure(state='disabled', text='', )
            trigger_sqrl4.place_forget()
        elif hole == 5:
            squirell_sound.play()
            trigger_sqrl5.configure(
                state='normal',
                image=squirell, )
            trigger_sqrl5.place(x=790, y=400)
            sleep(0.75)
            trigger_sqrl5.configure(state='disabled', text='', )
            trigger_sqrl5.place_forget()
        elif hole == 6:
            squirell_sound.play()
            trigger_sqrl6.configure(
                state='normal',
                image=squirell, )
            trigger_sqrl6.place(x=210, y=530)
            sleep(0.75)
            trigger_sqrl6.configure(state='disabled', text='', )
            trigger_sqrl6.place_forget()
        elif hole == 7:
            squirell_sound.play()
            trigger_sqrl7.configure(
                state='normal',
                image=squirell, )
            trigger_sqrl7.place(x=600, y=530)
            sleep(0.75)
            trigger_sqrl7.configure(state='disabled', text='', )
            trigger_sqrl7.place_forget()
        elif hole == 8:
            squirell_sound.play()
            trigger_sqrl8.configure(
                state='normal',
                image=squirell, )
            trigger_sqrl8.place(x=1000, y=520)
            sleep(0.75)
            trigger_sqrl8.configure(state='disabled', text='', )
            trigger_sqrl8.place_forget()
    county.place_forget()
    if score > highscore and score != 1000:
        background_music.stop()
        new_highscore.play()
        highscore = score
        highscore_dekhau.configure(text=f"High Score: {score}")
        kailesurugarne.place(x=570, y=130)
        kailesurugarne.configure(text="New High Score!!!")
        sleep(5)
        kailesurugarne.place_forget()
    elif score == 700:
        victory.play()
        background_music.stop()
        highscore = score
        highscore_dekhau.configure(text=f"High Score: {score}")
        kailesurugarne.place(x=570, y=130)
        kailesurugarne.configure(text="You Won!!!", fg_color="black")
        sleep(15)
        kailesurugarne.configure(fg_color='white')
    else:
        sleep(2)
    playbtn.place(x=600, y=450)
    htp.place(x=550, y=520)


# when the game starts, this function initiates the countdown... "ready", "set", "whack!!!"
def ready_set_whack():
    kailesurugarne.configure(text="Ready", )
    sleep(1)
    kailesurugarne.configure(text="Set")
    sleep(1)
    kailesurugarne.configure(text="WHACK!!")
    sleep(1)
    kailesurugarne.place_forget()


def how():
    htp.place_forget()
    menu.place(relx=0.5, rely=0.5, anchor=CENTER)
    playbtn.place(x=1250, y=700)


# these are all just the buttons and labels that willl be used throughout the code.. aka variables ig?


# MUSIC!!!!
pygame.mixer.init()
background_music = pygame.mixer.Sound("background_music.mp3")
squirell_sound = pygame.mixer.Sound("squirell sound.mp3")
new_highscore = pygame.mixer.Sound("new_highscore.mp3")
victory = pygame.mixer.Sound("victoryy.mp3")

# background image!!!
homepic = customtkinter.CTkImage(Image.open("home screen.png"), size=(width, height))
Home_screen = customtkinter.CTkLabel(app, image=homepic, text='')
Home_screen.place(relx=0.5, rely=0.5, anchor=CENTER)

# scoreboard label!!
score_label = customtkinter.CTkLabel(master=Home_screen,
                                     text=f"Score:{score}",
                                     bg_color="#1d5731",  # 21c65a
                                     width=220,
                                     height=50,
                                     font=("PokemonGB", 25,),
                                     text_color="white"
                                     )
score_label.place(x=110, y=130)

# High score board!
highscore_dekhau = customtkinter.CTkLabel(master=Home_screen,
                                          text=f"High Score: {highscore}",
                                          bg_color="#21c65a",
                                          width=10,
                                          height=50,
                                          font=("PokemonGB", 25),
                                          text_color="Black"
                                          )
highscore_dekhau.place(x=960, y=130)

# Countdown !!!

county = customtkinter.CTkLabel(master=Home_screen, font=("PokemonGB", 30), text=f"Squirells Left:{countdown}")

# rat image
squirell = customtkinter.CTkImage(Image.open("squirrel.png"), size=(160, 160))
howpic = customtkinter.CTkImage(Image.open("how.png"), size=(1000, 650))

# rat image when it is clicked aka. hit
bonked = customtkinter.CTkImage(Image.open("squirrel_on_mud.png"), size=(170, 160))

# the "ready!" "set!" "go!" ko placeholder
kailesurugarne = customtkinter.CTkLabel(text='',
                                        master=Home_screen,
                                        bg_color="Black",
                                        corner_radius=0,
                                        fg_color="white",
                                        width=250,
                                        height=50,
                                        font=("PokemonGB", 30),
                                        text_color="black"
                                        )

# play button
playbtn = customtkinter.CTkButton(master=Home_screen,
                                  text="Start",
                                  font=("PokemonGB", 30),
                                  command=start,
                                  width=80,
                                  height=60,
                                  border_width=5,
                                  corner_radius=5,
                                  border_spacing=5,
                                  bg_color='#21c65a',
                                  border_color="#062b44",
                                  hover=False
                                  )
playbtn.place(x=600, y=450)

# how to play button

htp = customtkinter.CTkButton(master=Home_screen,
                              text="How to play?",
                              font=("PokemonGB", 30),
                              command=how,
                              width=80,
                              height=60,
                              border_width=5,
                              corner_radius=5,
                              border_spacing=5,
                              bg_color='#21c65a',
                              border_color="#062b44",
                              hover=False
                              )
htp.place(x=550, y=520)

menu = customtkinter.CTkLabel(master=Home_screen,
                              image=howpic,
                              text=''
                              )
# menu.place(relx =0.5,rely =0.5, anchor =CENTER)
# squirell1
trigger_sqrl1 = customtkinter.CTkButton(master=Home_screen,
                                        command=onwhack,
                                        text='',
                                        state='disabled',
                                        fg_color='#21c65a',
                                        height=10,
                                        width=10,
                                        corner_radius=0,
                                        hover=False,
                                        )

# squirell2
trigger_sqrl2 = customtkinter.CTkButton(master=Home_screen,
                                        command=onwhack,
                                        text='',
                                        state='disabled',
                                        fg_color='#21c65a',
                                        height=10,
                                        width=10,
                                        corner_radius=0,
                                        hover=False,
                                        )

# squirell3
trigger_sqrl3 = customtkinter.CTkButton(master=Home_screen,
                                        command=onwhack,
                                        text='',
                                        state='disabled',
                                        fg_color='#21c65a',
                                        height=10,
                                        width=10,
                                        corner_radius=0,
                                        hover=False,
                                        )

# squirell4
trigger_sqrl4 = customtkinter.CTkButton(master=Home_screen,
                                        command=onwhack,
                                        text='',
                                        state='disabled',
                                        fg_color='#21c65a',
                                        height=10,
                                        width=10,
                                        corner_radius=0,
                                        hover=False,
                                        )

# squirell5
trigger_sqrl5 = customtkinter.CTkButton(master=Home_screen,
                                        command=onwhack,
                                        text='',
                                        state='disabled',
                                        fg_color='#21c65a',
                                        height=10,
                                        width=10,
                                        corner_radius=0,
                                        hover=False,
                                        )

# squirell6
trigger_sqrl6 = customtkinter.CTkButton(master=Home_screen,
                                        command=onwhack,
                                        text='',
                                        state='disabled',
                                        fg_color='#21c65a',
                                        height=10,
                                        width=10,
                                        corner_radius=0,
                                        hover=False,
                                        )

# squirell7
trigger_sqrl7 = customtkinter.CTkButton(master=Home_screen,
                                        command=onwhack,
                                        text='',
                                        state='disabled',
                                        fg_color='#21c65a',
                                        height=10,
                                        width=10,
                                        corner_radius=0,
                                        hover=False,
                                        )

# squirell8
trigger_sqrl8 = customtkinter.CTkButton(master=Home_screen,
                                        command=onwhack,
                                        text='',
                                        state='disabled',
                                        fg_color='#21c65a',
                                        height=10,
                                        width=10,
                                        corner_radius=0,
                                        hover=False,
                                        )

app.mainloop()
