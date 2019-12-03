#Christopher Marotta and William Adu-Jamfi
#December 3rd, 2019
#Video Poker Project

from tkinter import *
#from PIL import ImageTk

#Create Tkinter window variables
window = Tk()
#Create general variables

#Create user class
class Player:
    #Initializes variables within the Player class
    def __init__(self, fn = "first", ln = "Last", b = 100):
        self.__firstname = fn
        self.__lastname = ln
        self.__balance = b

    #Returns first name of the player
    def getfirstname(self):
        return self.__firstname

    #Returns last name of the player
    def getlastname(self):
        return self.__lastname

    #Returns balance of the player
    def getbalance(self):
        return self.__balance

   #Returns username of the player
    def username(self):
        self.__username = username
        return self.__username

   #Returns Password of the Player
    def password(self):
        self.__password = password
        return self.__password

    

    
    

#create game class


window.mainloop()
