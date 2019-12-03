#Christopher Marotta and William Adu-Jamfi
#December 3rd, 2019
#Video Poker Project

from tkinter import *
from PIL import ImageTk

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
class Game:
    #Constructs the Game Object with an input of a list of users.
    def __init__(userList):
        #Saves the userList as a variable called users.
        users = userList
        #Sets a placeholder variable for a logged in user.
        currentUser = None
        #A list of cards that have been drawn, False = Not Drawn & True = Drawn
        drawnCards = []
        #Goes through 0 to 51 setting it to i
        for i in range(52):
            #Sets the value of drawnCards[i] to False to represent an undrawn card.
            drawnCards.append(False)
        #Creates a list that will be used to hold card images.
        cardDeck = []
        #Goes through 0 to 51 setting it to i
        for i in range(52):
            #Adds 1 to i then based on the number it will save that card image in the deck.
            cardDeck.append(ImageTK.PhotoImage(file="card/"+str((i+1))+".gif"))
        #Save the card background to be used.
        cardBackground = ImageTK.PhotoImage(file="card/b2fv.gif")
        #Moves to the function which allows a user to login.
        self.userLogin(self.users)
        return
    
    #Processes a user login event.
    def userLogin(users):
        #Creates a frame to store all of the widgets related to logging in.
        loginFrame = Frame(window)


#Starts the program
window.mainloop()
