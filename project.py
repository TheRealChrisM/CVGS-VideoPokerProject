#Christopher Marotta and William Adu-Jamfi
#December 3rd, 2019
#Video Poker Project

from tkinter import *
from PIL import ImageTk
import random

#Create Tkinter window variables
window = Tk()
#Creates a frame to store all of the widgets related to logging in.
loginFrame = Frame(window)
forgotPasswordFrame = Frame(window)
gameFrame = Frame(window)

#Create general variables

#Creates a StringVar for username to be used when logging in.
username = StringVar()
#Creates a StringVar for password to be used when logging in.
password = StringVar()
#Creates a stringVar for the response to a forgotten password screen.
forgotPasswordInput = StringVar()
#Creates a variable to store the correct response to the forgotten password screen.
forgotPasswordInputAnswer = ""
#Creates a variable to temporarily store the correct password for the user.
correctPassword = ""
#Creates the userlist which will be used to store user accounts.
userList = []
#Creates placeholder cardButton variables so they can be used between functions.
cardOneButton = None
cardTwoButton = None
cardThreeButton = None
cardFourButton = None
cardFiveButton = None
cardDeckButton = None

#Create user class
class Player:
    #Initializes variables within the Player class
    def __init__(self, fn = "first", ln = "Last", user = "username", pw = "password", pq = "passwordhintQuestion", ph = "passwordhint", b = 100):
        self.__firstname = fn
        self.__lastname = ln
        self.__username = user
        self.__password = pw
        self.__balance = b
        self.__passwordhintQuestion = pq
        self.__passwordhint = ph
        return

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
    def getusername(self):
        return self.__username

   #Returns Password of the Player
    def getpassword(self):
        self.__password = password
        return self.__password

    #Returns a boolean based on whether the input matches the user's password
    def passwordCheck(self, input):
        passMatch = False
        if self.__password == input:
            passMatch = True
        return passMatch
    
    #Fetches the password hint for the Player
    def getpasswordhint(self):
        return self._passwordhint
   
    #Creates new password hint based on user input 
    def setpasswordhint(self):
        self.__passwordhint = newpassword
        return self.__passwordhint

    #Fetches the password hint question for the Player
    def getpasswordhintQuestion(self):
        return self.__passwordhintQuestion

    #Returns the password hint of the Player
    def passwordhint(self):
        return self.__passwordhint

#create game class
class Game:
    #Constructs the Game Object with an input of a list of users.
    def __init__(self, userList):
        #Saves the userList as a variable called users.
        self.__users = userList
        #Sets a placeholder variable for a logged in user.
        self.__currentUser = None
        #A list of cards that have been drawn, False = Not Drawn & True = Drawn
        self.__drawnCards = []
        #Goes through 0 to 51 setting it to i
        for i in range(52):
            #Sets the value of drawnCards[i] to False to represent an undrawn card.
            self.__drawnCards.append(False)
        #Creates a list that will be used to hold card images.
        self.__cardDeck = []
        #Goes through 0 to 51 setting it to i
        for i in range(52):
            #Adds 1 to i then based on the number it will save that card image in the deck.
            self.__cardDeck.append(ImageTk.PhotoImage(file="card/"+str((i+1))+".gif"))
        #Save the card background to be used.
        self.__cardBackground = ImageTk.PhotoImage(file="card/b2fv.gif")
        #Moves to the function which allows a user to login.
        self.__userHand = [0,0,0,0,0]
        self.__userHandImage = ["","","","",""]
        self.userLogin()
        return
    
    def setUser(self, curUser):
        self.__currentUser = curUser
        return

    def getHand(self, index):
        return self.__userHand[index]
    
    def getUser(self):
        return self.__currentUser

    def setUserHandImage(self, index, imageNum):
        self.__userHandImage[index] = ImageTk.PhotoImage(file="card/"+str(self.getcard(imageNum))+".gif")
        return

    def getUserHandImage(self, index):
        return self.__userHandImage[index]
    
    #Creates a function that draws a random card
    def newcard(self):
        randomCard = random.randint(0,51)
        while (self.drawn(randomCard)):
           randomCard = random.randint(0,51)
        self.setDrawn(randomCard)
        return (randomCard + 1)

    #Adds new cards to a player's hand
    def addcard(self, cardIndex):
        self.__userHand[cardIndex] = self.newcard()
        return

    def getcard(self, cardIndex):
        return self.__userHand[cardIndex]

    #Creates a function that returns True if the card has been selected
    def drawn(self, newcard):
        return self.__drawnCards[newcard]

    def setDrawn(self, newcard):
        self.__drawnCards[newcard] == True
        return
    
    #Deals a certain amount of cards to the players
    def deal(self):
        if not (cardOneButton["state"] == "disabled"):
            self.addcard(0)
            self.setUserHandImage(0,0)                                             
            cardOneButton["image"] = self.getUserHandImage(0)
        if not (cardTwoButton["state"] == "disabled"):
            self.addcard(1)
            self.setUserHandImage(1,1)                                             
            cardOneButton["image"] = self.getUserHandImage(1)
        if not (cardThreeButton["state"] == "disabled"):
            self.addcard(2)
            self.setUserHandImage(2,2)                                             
            cardOneButton["image"] = self.getUserHandImage(2)
        if not (cardFourButton["state"] == "disabled"):
            self.addcard(3)
            self.setUserHandImage(3,3)                                             
            cardOneButton["image"] = self.getUserHandImage(3)
        if not (cardFiveButton["state"] == "disabled"):
            self.addcard(4)
            self.setUserHandImage(4,4)                                             
            cardOneButton["image"] = self.getUserHandImage(4)
        
    
        #while i > 0 and False in cardDeck:
         #   drawcard = newcard()
          #  if not(draw(drawcard)):
           #     listofcards.addcard(Deck(drawcard))
            #    cardDeck[drawcard] = True
             #   i -= 1
              #  return

    #Returns Face Down Card
    def getcardbackground(self):
        return self.__cardBackground

    #Adds and Returns New Card 
    def getcarddeck(self):
        return self.__cardDeck
    
    #Processes a user login event.
    def userLogin(self):
        #Sets window title to "Login".
        window.title("Login")
        #Sets window width and height to 
        window.geometry("250x150")
        #Creates a Login Label.
        loginLabel = Label(loginFrame, text = "LOGIN", font=("times new roman bold", 16))
        #Creates a Username label.
        usernameLabel = Label(loginFrame, text = "Username: ")
        #Creates a Password Label.
        passwordLabel = Label(loginFrame, text = "Password: ")
        #Allows the user to input the username.
        usernamePrompt = Entry(loginFrame, textvariable = username)
        #Allows the user to input the password.
        passwordPrompt = Entry(loginFrame, textvariable = password, show = "*")
        #Creates a submit button that runs the processLogin function when run.
        submitButton = Button(loginFrame, text = "SUBMIT", command = self.processLogin)
        #Creates a button to switch to the forgot password screen.
        forgotPasswordButton = Button(loginFrame, text = "Forgot Password", command = self.forgotPassword)
        #Grids the Login screen label.
        loginLabel.grid(row = 0, columnspan = 2, pady = 5)
        #Grids the username label.
        usernameLabel.grid(row = 1, column = 0, pady = 10)
        #Grids the password label.
        passwordLabel.grid(row = 2, column = 0, pady = 10)
        #Grids the username entry box.
        usernamePrompt.grid(row = 1, column = 1)
        #Grids the password entry box.
        passwordPrompt.grid(row = 2, column = 1)
        #Grids the submit login button.
        submitButton.grid(row = 3, column = 0)
        forgotPasswordButton.grid(row = 3, column = 1)
        #Packs the login frame into the window.
        loginFrame.pack()
        return

    def processLogin(self):
        userFound = False
        savedUser = None
        selectedUser = username.get()
        for i in range(len(userList)):
                if (userList[i].getusername() == selectedUser):
                    userFound = True
                    savedUser = userList[i]
        if not userFound:
            messagebox.showinfo("No user", "User not found.")
        elif userFound:
            if savedUser.passwordCheck(password.get()):
                self.setUser(savedUser)
                self.beginGame()
            else:
                messagebox.showinfo("Login Attempt", "Incorrect login credentials. Attempt will be logged.")
                password.set("")
        return

    def forgotPassword(self):
        global forgotPasswordInputAnswer, correctPassword
        loginFrame.pack_forget()
        selectedUser = username.get()
        savedUser = None
        userFound = False
        for i in range(len(userList)):
                if (userList[i].getusername() == selectedUser):
                    userFound = True
                    savedUser = userList[i]
        if not userFound:
            messagebox.showinfo("User Not Found", "User could not be found.")
            self.userLogin()
        forgotPasswordInputAnswer = savedUser.passwordhint()
        correctPassword = savedUser.passwordhint()
        passwordHintPromptText = savedUser.getpasswordhintQuestion()
        passwordHintPromptLabel = Label(forgotPasswordFrame, text = passwordHintPromptText, wraplength = 250, justify = LEFT, pady = 5)
        passwordHintEntry = Entry(forgotPasswordFrame, textvariable = forgotPasswordInput)
        passwordHintButton = Button(forgotPasswordFrame, text = "SUBMIT", command = self.checkPasswordHint)
        #passwordHintButton = Button(forgotPasswordFrame, text = SUBMIT, command = check
        #passwordHintButton = Button(forgotPasswordFrame, text = "SUBMIT", command = self.checkPassword)
        passwordHintPromptLabel.grid(row = 0, column = 0)
        passwordHintEntry.grid(row = 1, column = 0)
        passwordHintButton.grid(row = 2, column = 0)
        forgotPasswordFrame.pack()
        return

    def checkPasswordHint(self):
        global forgotPasswordInputAnswer, correctPassword
        print(forgotPasswordInputAnswer, correctPassword)
        if (forgotPasswordInput.get() == forgotPasswordInputAnswer):
            messagebox.showinfo("Password", ("Your password is:\n " + correctPassword))
            correctPassword = ""
            forgotPasswordInputAnswer = ""
            passwordHintPromptText = ""
            forgotPasswordInput.set("")
            forgotPasswordFrame.pack_forget()
            self.userLogin()
        else:
            messagebox.showinfo("Password Hint", "Your response was incorrect.\n\n Returning to login screen.")
            correctPassword = ""
            forgotPasswordInputAnswer = ""
            passwordHintPromptText = ""
            forgotPasswordInput.set("")
            forgotPasswordFrame.pack_forget()
            self.userLogin()
        return

    def beginGame(self):
        
        global cardOneButton, cardTwoButton, cardThreeButton, cardFourButton, cardFiveButton, cardDeckButton
        loginFrame.pack_forget()
        window.title("Video Game Poker")
        window.geometry("700x300")
        playerNameLabel = Label(gameFrame, text = (self.getUser().getfirstname() + " " + self.getUser().getlastname()), anchor = "w")
        playerBalanceLabel = Label(gameFrame, text = ("Balance: " + str(self.getUser().getbalance())), anchor = "w")
        exitGameButton = Button(gameFrame, text = "EXIT", command = self.exitGame)
        playerNameLabel.grid(row = 0, column = 0)
        playerBalanceLabel.grid(row = 1, column = 0)
        cardOneButton = Button(gameFrame, image = self.getcardbackground(), command = self.processCardOne)
        cardTwoButton = Button(gameFrame, image = self.getcardbackground(), command = self.processCardTwo)
        cardThreeButton = Button(gameFrame, image = self.getcardbackground(), command = self.processCardThree)
        cardFourButton = Button(gameFrame, image = self.getcardbackground(), command = self.processCardFour)
        cardFiveButton = Button(gameFrame, image = self.getcardbackground(), command = self.processCardFive)
        cardDeckButton = Button(gameFrame, image = self.getcardbackground(), command = self.processCardDeck)
        cardDeckButton.grid(row = 2, column = 0, padx = 50)
        cardOneButton.grid(row = 2, column = 1, padx = 5)
        cardTwoButton.grid(row = 2, column = 2, padx = 5)
        cardThreeButton.grid(row = 2, column = 3, padx = 5)
        cardFourButton.grid(row = 2, column = 4, padx = 5)
        cardFiveButton.grid(row = 2, column = 5, padx = 5)
        exitGameButton.grid(row = 0, column = 100)
        gameFrame.grid(row = 0, column = 0)
        return

    def processCardOne(self):
        if not (str(cardTwoButton["image"]) == str(self.getcardbackground())):
            cardOneButton["state"] = "disabled"
        return

    def processCardTwo(self):
        if not (str(cardTwoButton["image"]) == str(self.getcardbackground())):
            cardTwoButton["state"] = "disabled"
        return

    def processCardThree(self):
        if not (str(cardThreeButton["image"]) == str(self.getcardbackground())):
            cardThreeButton["state"] = "disabled"
        return

    def processCardFour(self):
        if not (str(cardFourButton["image"]) == str(self.getcardbackground())):
            cardFourButton["state"] = "disabled"
        return

    def processCardFive(self):
        if not (str(cardFiveButton["image"]) == str(self.getcardbackground())):
            cardFiveButton["state"] = "disabled"
        return

    def processCardDeck(self):
        self.deal()
        return

    def exitGame(self):
        window.destroy()
        return
    
    def checkPassword(self):
        return


    def winningstable(self):
        # Show winnings table
        lbl = Label(Game, text="Winnings Table", relief=RAISED)
        lbl.grid

        #Shows Text for Winnings Table
        wte = {250: "Royal Flush", 50: "Straight Flush",
               25: "Four of a Kind", 9: "Full House", 6: "Flush",
               4: "Straight", 3: "Three of a Kind", 2: "Two Pair",
               1: "Jacks or Higher"}

        return

    def getScore(self):
        score = 0
        if self.isRoyalFlush():
            score = 250
        elif self.isStraightFlush(): 
            score = 50
        elif self.isFourOfAKind():
            score = 25
        elif self.isFullHouse():
            score = 9
        elif self.isFlush():
            score = 6
        elif self.isStraight():
            score = 4
        elif self.isThreeOfAKind():
            score = 3
        elif self.isTwoPair():
            score = 2
        elif self.isTwoPair():
            score = 1
        else:
            score = 0  
        return score

#Add default users
userList.append(Player("King", "Howard", "kh", "cvgs", "Is Computer Science a real Science?", "True"))
userList.append(Player("Mickey", "Mouse", "mmouse", "Disney", "Where I work.", "Disney"))
userList.append(Player("John", "Doe", "jd", "bruh", "This is a test to see how long you can make password hints before things start getting weird so that we don't loose points for super duper long password hints.", "bruh"))
game = Game(userList)

#Starts the program
window.mainloop()
