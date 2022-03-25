from unittest import result
from detoxify import Detoxify
from logging import exception
from operator import index
from pickle import FALSE
from tkinter import E
from tokenize import String
from statistics import mean
import pandas as pd
import numpy
import sys
import requests
import mysql
import math
import time

def main():
   matchid = (5490010545) #match ID query
   list = []
   while True:  #keep going
        response=None
        while response==None:   #"if match id is empty"
            response = getdata(matchid)
        list = findplayers(response,list)
        findchats(response,list)
        #inserttoDB(list)       #if our SQL would have worked
        list=None
        matchid=matchid+1
        print("hello")

def getdata(matchid): # Calling the dota api for gamedata

    time.sleep(0.5)     #Sometimes the API give quits, if we are too fast. theres also a hard limit on request
    try:
        response = requests.get('https://api.opendota.com/api//matches/'+str(matchid))
        datachat=response.json()["chat"]
    except:
        return None
    return response



def findplayers(response,list):# find player name and spots on the team
    seats = response.json()["players"]
    index = 0
    list = []
    while index < len(seats):
        playerslot = (seats[index]["player_slot"])
        try: 
            playerName = seats[playerslot]["personaname"]
            list.append(Player(playerslot,playerName))
        except:
            list.append(Player((playerslot,None)))
        index = index + 1
    return list

def findchats(response,list): # recording chat messages and asigning a behaviour score
    game = response.json()["players"]
    chat = response.json()["chat"]

    try: # if the game lacs chat data
        index = 0
        while index < len(chat) - 1:
            if chat[index]["type"] == "chat":
                chatlog = chat[index]["key"]
                slot = (chat[index]["slot"])
                behavior=(Detoxify('original').predict(chatlog))
                bscore=getmean(behavior)
                list[slot].addmorechat(chatlog)
                list[slot].addbehaviur(bscore)
            index = index + 1
    except:
        return FALSE


def getmean(results): # thanks to detoxify for the neural engine https://github.com/unitaryai/detoxify
    
    for a in results: 
        mean= mean + results.get(a)
    result=(mean/len(results))
    print (result)
    return result

class Player: #storing player value
    Index = 0

    def __init__(self,seat, name="ano"):
        Player.Index=Player.Index+1
        self.name = name
        self.chat = ""
        self.seat = seat
        self=behaviour=0.5


    def addmorechat(self,chat): #ading chat messages
        self.chat= self.chat+", "+chat
        print(chat)

    
    def addbehaviur(self,behaviur):
        print(behaviur)
        self.behaviur= (self.behaviur+behaviur)/2

       


if __name__ == "__main__":
    main()