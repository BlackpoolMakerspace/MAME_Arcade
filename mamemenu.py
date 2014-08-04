#Python Mame Menu

import easygui as eg
import os

choice = ["chasehq","tmnt","rtype"]
logo = "/home/les/Downloads/MAME.gif"

start = eg.buttonbox(title="Blackpool Makerspace Arcade Cabinet",image=logo,msg="Would you like to play a game?",choices=["Yes","No"])

while True:
    if start != "No":
        game = eg.choicebox(msg='What game would you like?', title='Blackpool Makerspace Arcade Cab', choices=(choice))
        os.system("mame "+(game))
    else:
        print("EXIT")
        break
