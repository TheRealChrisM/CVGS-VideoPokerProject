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
registerFrame = Frame(window)
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
#Creates a stringvar to save the recovery question when creating an account.
recoveryQuestion = StringVar()
#Creates a stringvar to save the recovery answer for creating an account.
recoveryAnswer = StringVar()
#Creates a stringvar to store the first name when creating an account.
firstName = StringVar()
#Creates a stringvar to store the last name when creating an account.
lastName = StringVar()
#Creates placeholder cardButton variables so they can be used between functions.
cardOneButton = None
cardTwoButton = None
cardThreeButton = None
cardFourButton = None
cardFiveButton = None
cardDeckButton = None
currentBet = None
increaseBetButton = None
decreaseBetButton = None

#Create user class
class Player:
    #Initializes variables within the Player class
    def __init__(self, fn = "first", ln = "Last", user = "username", pw = "password", pq = "passwordhintQuestion", ph = "passwordhint", b = 100):
        self.__firstname = fn #Saves the first name input for the object.
        self.__lastname = ln #Saves the last name input for the object.
        self.__username = user #saves the username input for the object.
        self.__password = pw #Saves the password input for the object.
        self.__balance = b #Saves the balance input for the object.
        self.__passwordhintQuestion = pq #Saves the password hint question for the object.
        self.__passwordhint = ph #Saves the password hint answer for the object.
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
        return self.__password

    #adds a setbalance to the player
    def addbalance(self, addAmt):
        self.__balance = self.__balance + addAmt
        return

    #Removes the balance for the player after a bet
    def removebalance(self, removeAmt):
        self.__balance = self.__balance - removeAmt

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


class Card(): #Creates a class for the card deck
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] #Creates a list for the card ranks
    suits = ['S', 'D', 'H', 'C'] #Creates a list for the card suits
    

    def __init__ (self, rank, suit):
        self.rank = rank #Creates an initialized variable for the card ranks
        self.suit = suit #Creates an initialized variable for the card suits
        if (suit == 0):
            self.suit = self.suits[0]
        elif (suit == 1):
            self.suit = self.suits[2]
        elif (suit == 2):
            self.suit = self.suits[1]
        elif (suit == 3 or suit == 4):
            self.suit = self.suits[3]

    def __str__ (self):
        if self.rank == 1:
          rank = 'A' #Returns as an Ace if the card rank is 1
        elif self.rank == 13 or self.rank == 0:
          rank = 'K' #Returns as a King if the card rank is 13
        elif self.rank == 12:
          rank = 'Q' #Returns as a Queen if the card rank is 12
        elif self.rank == 11:
          rank = 'J' #Returns as a Jack if the card rank is 11
        else:
          rank = str(self.rank) #Otherwise, it returns the rank's number
        return str(rank) + self.suit #Returns a string of the rank and suit


#create game class
class Game:
    #Constructs the Game Object with an input of a list of users.
    def __init__(self, userList):
        #Returns the Card's rank and suit
        for suit in Card.suits:
            for rank in Card.ranks:
                card = Card(rank, suit)
        self.tlist = []
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
        #Creates a list which stores the card numbers in the user's hand.
        self.__userHand = [0,0,0,0,0]
        #Creates a list which stores the image values in the user's hand
        self.__userHandImage = ["","","","",""]
        #Moves to the function which allows a user to login.
        self.userLogin()
        #A variable representing the user's current bet.
        self.__curBet = 1
        #Variable representings draws in a round
        self.__drawNumber = 0
        return

    #Returns the value of draw number.
    def getDraws(self):
        #returns the current draw number
        return self.__drawNumber

    #Change the value of draw number
    def setDraws(self, newVal):
        #Sets the value based on the input
        self.__drawNumber = newVal
        return

    #A functions which displays the current bet value.
    def currentBet(self):
        return self.__curBet
    
    #A fucntion which increases the user's bet by 1 if their balance allows.
    def increaseBet(self):
        #Ensures that the player can actually make the bet change.
        if (self.getUser().getbalance() >= (self.currentBet()+1)) and (5 >= (self.currentBet()+1)):
            #Makes the bet change.
            self.__curBet = self.__curBet+1
            #Changes the current bet label.
            currentBet["text"] = self.__curBet
        return
    #A function which returns the userList
    def getListOfUsers(self):
        return self.__users
    
     #A fucntion which increases the user's bet by 1 if it is greater than zero.
    def decreaseBet(self):
        #Ensures that the player can actually make the bet change.
        if (0 < (self.currentBet()-1)):
            #Makes the bet change.
            self.__curBet = self.__curBet-1
            #Changes the currentBet Label
            currentBet["text"] = self.__curBet
        return
        
    #A function which sets the user that is currently playing and saves it for later use.
    def setUser(self, curUser):
        self.__currentUser = curUser #Creates a variable for the current user
        return

    #Returns a card number in the user's hand based on the index input.
    def getHand(self, index):
        #Finds the card in the user's hand and then returns it.
        return self.__userHand[index]

    #This function returns the current user so that player functions can be run on it.
    def getUser(self):
        return self.__currentUser #Fetches the current user

    #This function adds a user to the userlist, mainly used for registration.
    def addUser(self, newUser):
        #Appends the new user object to the current "database" of users.
        self.__users.append(newUser)
        return

    #Changes the saved image variable for a user's card hand.
    def setUserHandImage(self, index, imageNum):
        #Creates the new variable and saves it to the desired index.
        self.__userHandImage[index] = ImageTk.PhotoImage(file="card/"+str(self.getcard(imageNum))+".gif")
        return

    #Returns a image variable for the user's hand.
    def getUserHandImage(self, index):
        #Returns the image variable based on the desired index.
        return self.__userHandImage[index]
    
    #Creates a function that draws a random card
    def newcard(self):
        randomCard = random.randint(0,51) #Creates a random card from 0 to 51
        while (self.drawn(randomCard)): #Makes sure that the card has not already been drawn.
           randomCard = random.randint(0,51) #If it has keep drawing random cards.
        self.setDrawn(randomCard)#Once a new card has been drawn, set it to drawn so it is not drawn again.
        return (randomCard + 1) #Return the card's number +1 to represent that the cards are picked from 0-51 and not 1-52.

    #Adds new cards to a player's hand
    def addcard(self, cardIndex):
        #Draws a new card for the user's hand based on a desired index.
        self.__userHand[cardIndex] = self.newcard()
        return

    #Returns a specfic card from the user's hand.
    def getcard(self, cardIndex):
        #Returns the card number from the input index.
        return self.__userHand[cardIndex]

    #Creates a function that returns True if the card has been selected
    def drawn(self, newcard):
        #Return the value of the list at the newcard index.
        return self.__drawnCards[newcard]

    #Sets a card to drawn once it has been drawn
    def setDrawn(self, newcard):
        #Sets the appropriate index to true once it has been drawn.
        self.__drawnCards[newcard] = True
        return

    #A function which checks to see if a shuffle is required
    def checkShuffle(self):
        cardsLeft = 0
        for i in range(len(self.__drawnCards)):
            if (self.__drawnCards[i] == False):
                cardsLeft = cardsLeft + 1
        if cardsLeft < 6:
            for j in range(len(self.__drawnCards)):
                self.__drawnCards[j] = False
        return
        
    #Deals a certain amount of cards to the players
    def deal(self):
        #Global variables that are required because of limitations in tkinter
        global increaseBetButton, decreaseBetButton, cardOneButton, cardTwoButton, cardThreeButton, cardFourButton, cardFiveButton
        #Determines if the user still has enough money to play.
        timeToEnd = self.getUser().getbalance() <= 0
        #Makes sure the cards shouldn't be shuffled yet.
        self.checkShuffle()
        #If the user no longer has enough money.
        if timeToEnd:
            #End the game and display the credits.
            self.endgame()
        #Checks to see if the round is over yet.
        if (self.getDraws() < 2):
            #Checks to see if a user has marked a card to be held.
            if not (cardOneButton["state"] == "disabled"):
                #If they havent, draw a card and add it to their hand.
                self.addcard(0)
                #Find the correct card image and save it to the correct list.
                self.setUserHandImage(0,0)
                #Set the image to the card.
                cardOneButton["image"] = self.getUserHandImage(0)
            #Checks to see if a user has marked a card to be held.
            if not (cardTwoButton["state"] == "disabled"):
                #If they havent, draw a card and add it to their hand.
                self.addcard(1)
                #Find the correct card image and save it to the correct list.
                self.setUserHandImage(1,1)
                #Set the image to the card.
                cardTwoButton["image"] = self.getUserHandImage(1)
            #Checks to see if a user has marked a card to be held.
            if not (cardThreeButton["state"] == "disabled"):
                #If they havent, draw a card and add it to their hand.
                self.addcard(2)
                #Find the correct card image and save it to the correct list.
                self.setUserHandImage(2,2)
                #Set the image to the card.
                cardThreeButton["image"] = self.getUserHandImage(2)
            #Checks to see if a user has marked a card to be held.
            if not (cardFourButton["state"] == "disabled"):
                #If they havent, draw a card and add it to their hand.
                self.addcard(3)
                #Find the correct card image and save it to the correct list.
                self.setUserHandImage(3,3)
                #Set the image to the card.
                cardFourButton["image"] = self.getUserHandImage(3)
            #Checks to see if a user has marked a card to be held.    
            if not (cardFiveButton["state"] == "disabled"):
                #If they havent, draw a card and add it to their hand.
                self.addcard(4)
                #Find the correct card image and save it to the correct list.
                self.setUserHandImage(4,4)
                #Set the image to the card.
                cardFiveButton["image"] = self.getUserHandImage(4)
            #Changes the portion of the round the user is in for tracking purposes.
            self.setDraws(self.getDraws()+1)
            #Makes it so the user can't increase their bet.
            increaseBetButton["state"] = "disabled"
            #Makes it so the user can't decrease their bet.
            decreaseBetButton["state"] = "disabled"
            #Checks to see how many times the user has drawn cards.
            if (self.getDraws() == 2):
                #If more than two it runs the function again to end the round.
                self.deal()
        #If the user has finished the round.
        else:
            #Remove the amount they betted from their account.
            self.getUser().removebalance(self.currentBet())
            #Calculate the "Value" of their hand.
            self.calculateHand()
            #Reset the draw counter for tracking purposes.
            self.setDraws(0)
            #Set the bet back to 0.
            for i in range(5):
                #Runs the decreaseBet function the maximum amount of times to ensure that the bet is back to zero.
                self.decreaseBet()
            #Allow the user to increase their bet again.
            increaseBetButton["state"] = "active"
            #Allow the user to decrease their bet again.
            decreaseBetButton["state"] = "active"
            #Enables the first card button again.
            cardOneButton["state"] = "active"
            #Enables the second card button again.
            cardTwoButton["state"] = "active"
            #Enables the third card button again.
            cardThreeButton["state"] = "active"
            #Enables the fourth card button again.
            cardFourButton["state"] = "active"
            #Enables the fifth card button again.
            cardFiveButton["state"] = "active"
        return
    
    #Returns Face Down Card.
    def getcardbackground(self):
        #Returns the variable for a card that is face down.
        return self.__cardBackground

    #Adds and Returns New Card.
    def getcarddeck(self):
        #returns the card deck for undrawn cards.
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

    #A function which registers a new user.
    def registerUser(self):
        #Global variables that are required because of restrictions in tkinter.
        global recoveryQuestion, recoveryAnswer, firstName, lastName
        #Gets rid of the login frame.
        loginFrame.pack_forget()
        #The label which prompts for the user's first name.
        firstNameLabel = Label(registerFrame, text = "First: ")
        #An entry box to collect the user's first name.
        firstNameEntry = Entry(registerFrame, textvariable = firstName)
        #A label to ask for the user's last name.
        lastNameLabel = Label(registerFrame, text = "Last: ")
        #A entry box to collect the user's last name.
        lastNameEntry = Entry(registerFrame, textvariable = lastName)
        #Displays the prompt asking for a recovery question.
        newUserLabel = Label(registerFrame, text = "Please enter a password recovery question.")
        #An entry box that collects the user's desired recovery question.
        passwordRecoveryEntry = Entry(registerFrame, textvariable = recoveryQuestion)
        #Asks the user for the desired answer to their recovery question.
        passwordRecoveryAnswerLabel = Label(registerFrame, text = "What is the answer to this question?")
        #Gets the answer to the user's recovery question.
        passwordRecoveryAnswerEntry = Entry(registerFrame, textvariable = recoveryAnswer)
        #Creates a submit button to create the new user.
        registerSubmitButton = Button(registerFrame, text = "SUBMIT", command = self.submitRegistration)
        firstNameLabel.grid(row = 0, column = 0) #Grids the first name question.
        firstNameEntry.grid(row = 0, column = 1) #Grids the first name response.
        lastNameLabel.grid(row = 1, column = 0) #Grids the last name question.
        lastNameEntry.grid(row = 1, column = 1) #Grids the last name response.
        newUserLabel.grid(row = 2, columnspan = 2) #Grids the recovery question prompt.
        passwordRecoveryEntry.grid(row = 3, columnspan = 2) #Grids the recovery question response.
        passwordRecoveryAnswerLabel.grid(row = 4, columnspan = 2) #Grids the recovery question prompt.
        passwordRecoveryAnswerEntry.grid(row = 5, columnspan = 2) #Grids the recovery question response.
        registerSubmitButton.grid(row = 6, columnspan = 2) #Grids the submit button.
        #Displays the register frame.
        registerFrame.pack()
        return

    #A function which processes a user registration.
    def submitRegistration(self):
        newFirstName = firstName.get() #Saves the first name
        newLastName = lastName.get() #Saves the last name
        newUsername = username.get() #Saves the username
        newPassword = password.get() #Saves the password
        newRecoveryQuestion = recoveryQuestion.get() #Saves the recovery question
        newRecoveryAnswer = recoveryAnswer.get() #Saves the recovery answer
        #Creates a new user with the input.
        newUser = Player(newFirstName, newLastName, newUsername, newPassword, newRecoveryQuestion, newRecoveryAnswer)
        #Saves the new user.
        self.addUser(newUser)
        #Tells the user they have successfully registered.
        messagebox.showinfo("New User", (firstName.get() + ", you have successfully registered! \n Please log in!"))
        #Gets rid of the register frame.
        registerFrame.pack_forget()
        #Moves back to the user login.
        self.userLogin()
        return

    #A function which processes a login.
    def processLogin(self):
        #Placeholder variable for a boolean.
        userFound = False
        #placeholder variable for player.
        savedUser = None
        #Gets the user that should be found.
        selectedUser = username.get()
        #Looks through the userlist.
        for i in range(len(userList)):
                #Determines if a user is found.
                if (userList[i].getusername() == selectedUser):
                    #Indicates it is found.
                    userFound = True
                    #Sets the found user to a placeholder variable.
                    savedUser = userList[i]
        #Determines a user is not found.
        if not userFound:
            #Registers the new user.
            self.registerUser()
        #If the user is found.
            messagebox.showinfo("No user", "User not found.")
        elif userFound:
            #Checks the input and saved passwords.
            if savedUser.passwordCheck(password.get()):
                #If the password is correct it sets the user as the active user.
                self.setUser(savedUser)
                #Begins the game.
                self.beginGame()
            #In case that does not happen.
            else:
                #Game informs user that the password was incorrect.
                messagebox.showinfo("Login Attempt", "Incorrect login credentials. Attempt will be logged.")
                #Clears the password box.
                password.set("")
        return

    #A function which allows a user to get their password.
    def forgotPassword(self):
        #Global variables because of limitations in tkinter.
        global forgotPasswordInputAnswer, correctPassword
        #Gets rid of the login frame.
        loginFrame.pack_forget()
        #Saves the user's current inputted username.
        selectedUser = username.get()
        #Creates a player placeholder.
        savedUser = None
        #Creates a boolean to represent whether a user has been found.
        userFound = False
        #Goes through the user list.
        for i in range(len(self.getListOfUsers())):
                #If the username matches.
                if (self.getListOfUsers()[i].getusername() == selectedUser):
                    #Indicate a user was found.
                    userFound = True
                    #Save the found user.
                    savedUser = self.getListOfUsers()[i]
        #If the user was not found.
        if not userFound:
            #Display a message box informing them.
            messagebox.showinfo("User Not Found", "User could not be found.")
            #Take the user back to the login screen.
            self.userLogin()
        forgotPasswordInputAnswer = savedUser.passwordhint() #Retireve the user's password hint prompt answer.
        correctPassword = savedUser.getpassword() #Retireve the user's correct password.
        passwordHintPromptText = savedUser.getpasswordhintQuestion() #Retireve the user's password hint prompt.
        passwordHintPromptLabel = Label(forgotPasswordFrame, text = passwordHintPromptText, wraplength = 250, justify = LEFT, pady = 5) #Creates a label for the password hint question.
        passwordHintEntry = Entry(forgotPasswordFrame, textvariable = forgotPasswordInput) #Creates an entry box for the user to input the correct answer.
        passwordHintButton = Button(forgotPasswordFrame, text = "SUBMIT", command = self.checkPasswordHint) #Creates a button to submit their response.
        passwordHintPromptLabel.grid(row = 0, column = 0) #Displays the user's password prompt.
        passwordHintEntry.grid(row = 1, column = 0) #Displays the entry box.
        passwordHintButton.grid(row = 2, column = 0) #Displays the button.
        forgotPasswordFrame.pack() #Packs in the frame so it can be seen.
        return
    
    #A function that is used to check a submitted password hint response.
    def checkPasswordHint(self):
        #Global variables that are used because of limitations of tkinter.
        global forgotPasswordInputAnswer, correctPassword
        #Runs if the user correctly inputs the password recovery.
        if (forgotPasswordInput.get() == forgotPasswordInputAnswer):
            #Tells the user what the password is.
            messagebox.showinfo("Password", ("Your password is:\n " + correctPassword))
            #Resets the correctPassword variable
            correctPassword = ""
            #Resets the password recovery input.
            forgotPasswordInputAnswer = ""
            #Resets the password recovery question.
            passwordHintPromptText = ""
            #Resets the password recovery input.
            forgotPasswordInput.set("")
            #Removes the password recovery frame.
            forgotPasswordFrame.pack_forget()
            #Pushes the user back to login.
            self.userLogin()
        else:
            #Creates a message box if the ser gives an incorrect response to the password hint 
            messagebox.showinfo("Password Hint", "Your response was incorrect.\n\n Returning to login screen.")
            #Resets the correctPassword variable
            correctPassword = ""
            #Resets the password recovery input.
            forgotPasswordInputAnswer = ""
            #Resets the password recovery question.
            passwordHintPromptText = ""
            #Resets the password recovery input.
            forgotPasswordInput.set("")
            #Removes the password recovery frame.
            forgotPasswordFrame.pack_forget()
            #Pushes the user back to login.
            self.userLogin()
        return

    #A function used to begin the game.
    def beginGame(self):
        #Global variables that are used because of limitations of tkinter.
        global cardOneButton, cardTwoButton, cardThreeButton, cardFourButton, cardFiveButton, cardDeckButton, currentBet, increaseBetButton, decreaseBetButton
        #Removes the login frame.
        loginFrame.pack_forget()
        #Creates the title of the window as "Video Game Poker"
        window.title("Video Game Poker")
        #Creates the dimensions of the window 
        window.geometry("700x300")
        #Creates a label that fetches the player's first and last name
        playerNameLabel = Label(gameFrame, text = (self.getUser().getfirstname() + " " + self.getUser().getlastname()), anchor = "w")
        #Creates a balance label that fetches the player's balancce
        playerBalanceLabel = Label(gameFrame, text = ("Balance: " + str(self.getUser().getbalance())), anchor = "w")
        #Creates a button that exits the game
        exitGameButton = Button(gameFrame, text = "EXIT", command = self.exitGame)
        #Grids the Player name label
        playerNameLabel.grid(row = 0, column = 0)
        #Grids the Player balance label
        playerBalanceLabel.grid(row = 1, column = 0)
        cardOneButton = Button(gameFrame, image = self.getcardbackground(), command = self.processCardOne) #Creates a Button for Card 1
        cardTwoButton = Button(gameFrame, image = self.getcardbackground(), command = self.processCardTwo) #Creates a Button for Card 2
        cardThreeButton = Button(gameFrame, image = self.getcardbackground(), command = self.processCardThree) #Creates a Button for Card 3
        cardFourButton = Button(gameFrame, image = self.getcardbackground(), command = self.processCardFour) #Creates a Button for Card 4
        cardFiveButton = Button(gameFrame, image = self.getcardbackground(), command = self.processCardFive) #Creates a Button for Card 5
        cardDeckButton = Button(gameFrame, image = self.getcardbackground(), command = self.processCardDeck) #Creates a Button for Card Deck
        increaseBetButton = Button(gameFrame, text = "UP", command = self.increaseBet) #Creates a button which increases the bet.
        decreaseBetButton = Button(gameFrame, text = "DOWN", command = self.decreaseBet) #Creates a button which decreases the bet.
        currentBet = Label(gameFrame, text = "1") #Creates a label which displays the current bet.
        cardDeckButton.grid(row = 2, column = 0, padx = 50) #Grids the card deck to the gameFrame.
        cardOneButton.grid(row = 2, column = 1, padx = 5) #Grids the first card to the gameFrame.
        cardTwoButton.grid(row = 2, column = 2, padx = 5) #Grids the second card to the gameFrame.
        increaseBetButton.grid(row = 3, column = 2) #Grids the increase bet button.
        cardThreeButton.grid(row = 2, column = 3, padx = 5) #Grids the third card to the gameFrame.
        currentBet.grid(row = 3, column = 3) #Grids the current bet label.
        cardFourButton.grid(row = 2, column = 4, padx = 5) #Grids the fourth card to the gameFrame.
        decreaseBetButton.grid(row = 3, column = 4) #Grids the decrease bet button.
        cardFiveButton.grid(row = 2, column = 5, padx = 5) #Grids the fifth card to the gameFrame.
        exitGameButton.grid(row = 0, column = 100) #Grids the exit game button to the gameFrame.
        gameFrame.grid(row = 0, column = 0) #Grids the entire gameframe.
        cardDeckButton.grid(row = 2, column = 0, padx = 50) #Grids the Card Deck Button
        cardOneButton.grid(row = 2, column = 1, padx = 5) #Grids the Card One Button
        cardTwoButton.grid(row = 2, column = 2, padx = 5) #Grids the Card Two Button
        cardThreeButton.grid(row = 2, column = 3, padx = 5) #Grids the Card Three Button
        cardFourButton.grid(row = 2, column = 4, padx = 5) #Grids the Card Four Button
        cardFiveButton.grid(row = 2, column = 5, padx = 5) #Grids the Card Five Button
        return

    #This is run when the user clicks the first card.
    def processCardOne(self):
        #Checks to make sure that a card has been dealt.
        if not (str(cardOneButton["image"]) == str(self.getcardbackground())):
            #Allows the user to mark a card to be held so that a new one is not dealt.
            cardOneButton["state"] = "disabled"
        return

    #This is run when the user clicks the second card.
    def processCardTwo(self):
        #Checks to make sure that a card has been dealt.
        if not (str(cardTwoButton["image"]) == str(self.getcardbackground())):
            #Allows the user to mark a card to be held so that a new one is not dealt.
            cardTwoButton["state"] = "disabled"
        return

    #This is run when the user clicks the third card.
    def processCardThree(self):
        #Checks to make sure that a card has been dealt.
        if not (str(cardThreeButton["image"]) == str(self.getcardbackground())):
            #Allows the user to mark a card to be held so that a new one is not dealt.
            cardThreeButton["state"] = "disabled"
        return
    
    #This is run when the user clicks the fourth card.
    def processCardFour(self):
        #Checks to make sure that a card has been dealt.
        if not (str(cardFourButton["image"]) == str(self.getcardbackground())):
            #Allows the user to mark a card to be held so that a new one is not dealt.
            cardFourButton["state"] = "disabled"
        return

    #This is run when the user clicks the fifth card.
    def processCardFive(self):
        #Checks to make sure that a card has been dealt.
        if not (str(cardFiveButton["image"]) == str(self.getcardbackground())):
            #Allows the user to mark a card to be held so that a new one is not dealt.
            cardFiveButton["state"] = "disabled"
        return

    #This is run when the user clicks on the deck card.
    def processCardDeck(self):
        #Runs the deal function which deals a card to all "active" cards.
        self.deal()
        return

    def exitGame(self):
        window.destroy()  #Exits and destroys the window 
        return

    def winningstable(self):
        #Creates a button that shows the winnings table
        lbl = Label(gameFrame, text="Winnings Table", relief=RAISED)
        lbl.grid
        #Shows Text for Winnings Table
        wte = {250: "Royal Flush", 50: "Straight Flush",
               25: "Four of a Kind", 9: "Full House", 6: "Flush",
               4: "Straight", 3: "Three of a Kind", 2: "Two Pair",
               1: "Jacks or Higher"}
        return
    #Function which calculates the value of a player's hand 
    def calculateHand(self):
        #Saves a variable of the user's hand
        newHand = self.__userHand
        #Sorts the cards in the user's hand
        newHand = sorted(newHand, reverse = True)
        #Creates a placeholder variable to hold the new card objects
        fixedCards = []
        #Goes through each card in the hand
        for i in range(len(newHand)):
            #Saves the number of the card
            num = newHand[i]
            #Calculates the rank based on the saved number.
            rank = num%13
            #Calculates the suit based on the saved number
            suit = num//13
            #Creates a card object and saves it in the fixed cards list.
            fixedCards.append(Card(rank, suit))
        #Calculates the score based on your current hand.
        score = self.getScore(fixedCards)
        #Sets the score based on what the user bet
        score = score * self.currentBet()
        #Adds the balance to the user's balance.
        self.getUser().addbalance(score)
        #Displays a message saying how much the user made.
        messagebox.showinfo("Score", ("You got " +str(score)+ " points!"))
        #Goes to the next round.
        self.nextRound()
        return
        
    def point(self,sortedHand): #point()function to calculate partial score
        card_sum = 0 #Initializes the card sum
        ranklist = [] #Creates an empty list that stores the card rank
        for card in sortedHand: #For each card in the sorted list 
          ranklist.append(card.rank) #Adds the card rank to the empty list that stores rank
        card_sum = ranklist[0]*13**4+ranklist[1]*13**3+ranklist[2]*13**2+ranklist[3]*13+ranklist[4] #Creates value of the card sum
        return card_sum #Returns the card sum

    def isRoyalFlush(self, sortedHand): #Creates a function if the user has a Royal Flush  
        flag = True #Creates a variable that stores a Boolean value
        h = 10 #Stores an integer value
        Currentsuit = sortedHand[0].suit #Returns the current suit of the card
        Currentrank = 14 #Returns the current rank of the card
        total_point = h*13**5+self.point(sortedHand) #Returns the total points
        for card in sortedHand: #For each card in the sorted list
          if card.suit!= Currentsuit or card.rank!= Currentrank: #If the card suit or card rank is not equal to the current rank or suit, return False
            flag = False #Return false
            break
          else:
            Currentrank -= 1 #Else, subtract one from the current card rank 
        return flag


    def isStraightFlush(self, sortedHand): #Creates a function if the user has a Straight Flush 
        flag = True #Creates a variable that stores a Boolean value
        h = 9 #Stores an integer value
        Currentsuit = sortedHand[0].suit #Returns the current suit of the card  
        Currentrank = sortedHand[0].rank #Returns the current rank of the card
        total_point = h*13**5+self.point(sortedHand)#Returns the total points
        for card in sortedHand: #For each card in the sorted list 
          if card.suit!=Currentsuit or card.rank!=Currentrank: #If the card suit or card rank is not equal to the current rank or suit, return False
            flag=False #Return false
            break
          else:
            Currentrank -= 1 #Else, subtract one from the current card rank
        if flag:#If true
            flag = True
        else:
            flag = False
        return flag

    def isFourOfAKind(self, sortedHand): #Creates a function if the user has four of a kind
        flag = True #Creates a variable that stores a Boolean value
        h = 8 #Stores an integer value
        Currentrank=sortedHand[1].rank #Returns the current rank of the card
        count = 0 #Initializes the count variable as 0
        total_point = h*13**5+self.point(sortedHand) #Returns the total points
        for card in sortedHand: #For each card in the sorted list
          if card.rank == Currentrank: #If the card rank is equal to the current card rank
            count += 1 #Add 1 to the count
        if not count < 4: #If count is greater than 4
          flag = True #Returns true if the count is less than 4
        else:
            flag = False
        return flag

    def isFullHouse(self, sortedHand): #Creates a function if the user has a Full House
        flag = True #Creates a variable that stores a Boolean value
        h = 7 #Stores an integer value
        total_point = h*13**5+self.point(sortedHand) #Returns the total points
        mylist=[]#create a list to store ranks
        for card in sortedHand: #For each card in the sorted list 
          mylist.append(card.rank) #Adds the card rank to the empty mylist 
        rank1=sortedHand[0].rank #The 1st rank and the last rank should be different in a sorted list
        rank2=sortedHand[-1].rank #2nd rank in the sorted list
        numrank1= mylist.count(rank1) #Creates a variable to store the value of the 1st rank
        numrank2= mylist.count(rank2) #Creates a variable to store the value of the 2nd rank 
        if (numrank1==2 and numrank2==3)or (numrank1== 3 and numrank2== 2): #If the 1st rank is 2 and 2nd rank is 3, or 1st rank is 3 and 2nd rank is 2
          flag=True #Returns true
        else:
          flag=False #Creates a variable that creates a False Boolean value
        return flag

    def isFlush(self, sortedHand): #Creates a function if the user has a Flush       
        flag=True #Creates a variable that stores a Boolean value
        h = 6 #Stores an integer value
        total_point=h*13**5+self.point(sortedHand) #Returns the total points
        Currentsuit=sortedHand[0].suit #Returns the current suit of the card
        for card in sortedHand: #For each card in the sorted list 
          if not(card.suit == Currentsuit): #If card suit is not equal to the current suit
            flag=False #Return False
            break
        if flag: #Returns true
            flag = True
        else:
          flag = False
        return flag

    def isStraight(self, sortedHand): #Creates a function if the user has a straight
        flag = True #Creates a variable that stores a Boolean value
        h = 5 #Stores an integer value
        total_point = h*13**5+self.point(sortedHand) #Returns the total points
        Currentrank = sortedHand[0].rank  #this should be the highest rank
        for card in sortedHand:#For each card in the sorted list  
          if card.rank!= Currentrank: #If card rank is not equal to the current rank, return False
            flag = False #Return false
            break
          else:
            Currentrank -= 1 #Else, subtract one from the current card rank
        if flag: #Returns true
            flag = True
        else:
            flag = False
        return flag
        
    def isThreeOfAKind(self, sortedHand): #Creates a function if the user has three of a kind
        #sortedHand = sorted(hand,reverse=True) #Sorts the cards in the empty hand list
        flag = True #Creates a variable that stores a Boolean value
        h = 4 #Stores an integer value
        total_point = h*13**5+self.point(sortedHand) #Returns the total points
        Currentrank = sortedHand[2].rank #In a sorted rank, the middle one should have 3 counts if flag=True
        mylist = [] #create a list to store ranks
        for card in sortedHand: #For each card in the sorted list 
          mylist.append(card.rank) #Adds the card rank to the empty mylist
        if mylist.count(Currentrank)== 3: #If the current rank in mylist is equal to 3
          flag = True #Returns true
        else:
          flag=False #Return false
        return flag

    def isTwoPair(self, sortedHand):#Creates a function if the user has a TwoPair            
        flag = True #Creates a variable that stores a Boolean value
        h = 2 #Stores an integer value
        totalpoint = h*13**5+self.point(sortedHand) #Returns the total points
        mylist = [] #create an empty list to store ranks
        mycount = [] #create an empty list to store number of count of each rank
        for card in sortedHand: #For each card in sorted hand
          mylist.append(card.rank) #Adds a sorted card to the empty list
        for each in mylist: #For each card in mylist
          count = mylist.count(each) #Returns the count of each object in the list
          mycount.append(count) #Adds the count of each object to the mycount list
        if mycount.count(2)== 4 and mycount.count(1)== 1:  #There should be only 2sets of identical numbers and the rest are all different
          flag = True #Returns true
        else:
          flag = False #Return false
        return flag

    def isJacks(self, sortedHand):#Creates a function if the user has Jacks                
        flag = True #Creates a variable that stores a Boolean value
        h = 2 #Stores an integer value
        totalpoint = h*13**5+self.point(sortedHand) #Returns the total points
        mylist = [] #create an empty list to store ranks
        mycount = [] #create an empty list to store number of count of each rank
        for card in sortedHand: #For each card in sorted hand
          mylist.append(card.rank) #Adds a sorted card to the empty list
        for each in mylist: #For each card in mylist
          count = mylist.count(each) #Returns the count of each object in the list
          mycount.append(count) #Adds the count of each object to the mycount list
        if mycount.count(2)== 2 and mycount.count(1)== 3:  #There should be only 2 identical numbers and the rest are all different
          flag = True #Returns true
        else:
          flag = False #Return false
        return flag

    def getScore(self, hand):
        score = 0 #Initializes the scores
        if self.isRoyalFlush(hand): #Returns a score of 250 if it is a Royal Flush
            score += 250
        elif self.isStraightFlush(hand): #Returns a score of 50 if it is a Straight Flush
            score += 50
        elif self.isFourOfAKind(hand): #Returns a score of 25 if it is Four of a Kind
            score += 25
        elif self.isFullHouse(hand): #Returns a score of 9 if it is a Full House
            score += 9
        elif self.isFlush(hand): #Returns a score of 6 if it is a Flush
            score += 6
        elif self.isStraight(hand): #Returns a score of 4 if it is a Straight
            score += 4
        elif self.isThreeOfAKind(hand): #Returns a score of 3 if it is Three of a Kind
            score += 3
        elif self.isTwoPair(hand): #Returns a score of 2 if it is a Two Pair
            score += 2
        elif self.isJacks(hand): #Returns a score of a 1 if it is a Jacks
            score += 1
        return score


    def nextRound(self):
        self.beginGame()
        return

    def endgame(self):
        messagebox.showinfo("Game Over", "You have lost! Closing the window!")
        messagebox.showinfo("Credits", "William did the user class, card game logic such as Royal Flush, Straight Flush etc. while Chris did the user Login and password and gameplay.")
        window.destroy()
        return

#Add default users
userList.append(Player("King", "Howard", "kh", "cvgs", "Is Computer Science a real Science?", "True"))
userList.append(Player("Mickey", "Mouse", "mmouse", "Disney", "Where I work.", "Disney"))
userList.append(Player("John", "Doe", "jd", "bruh", "This is a test to see how long you can make password hints before things start getting weird so that we don't loose points for super duper long password hints.", "bruh"))
game = Game(userList)

#Starts the program
window.mainloop()
