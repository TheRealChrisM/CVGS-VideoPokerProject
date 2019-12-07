#Christopher Marotta and William Adu-Jamfi
#December 3rd, 2019
#Video Poker Project

from tkinter import *
from PIL import ImageTk

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
#passwordhint = input("What do you want your password hint to be: ")
userList = []

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
        self.userLogin()
        return
    
    def setUser(self, curUser):
        self.__currentUser = curUser
        return

    def getUser(self):
        return self.__currentUser

    #Creates a function that draws a random card and adds it to the deck 
    def newcard():
        newcardlist = []
        newcardlist.append(ImageTk.PhotoImage(file="card/"+str((i+1))+".gif"))
        newcardlist = random.randint(0,51)
        return newcard

    #Adds new card to a player's hand
    def addcard(self, newcard):
        self.__cardDeck.append(newcard)

    #Creates a function that returns True if the card has been selected
    def draw(newcard):
        return cardDeck[newcard]
        
    #Deals a certain amount of cards to the players
    def deal(listofcards, numofcards):
        i = numofcards
        while i > 0 and False in cardDeck:
            drawcard = newcard()
            if not(draw(drawcard)):
                listofcards.addcard(Deck(drawcard))
                cardDeck[drawcard] = True
                i -= 1
                return

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
        passwordHintButton = Button(forgotPasswordFrame, text = SUBMIT, command = check)
        passwordHintButton = Button(forgotPasswordFrame, text = "SUBMIT", command = self.checkPassword)
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
        loginFrame.pack_forget()
        window.title("Video Game Poker")
        playerNameLabel = Label(gameFrame, text = (self.getUser().getfirstname() + " " + self.getUser().getlastname()), anchor = "w")
        playerBalanceLabel = Label(gameFrame, text = ("Balance: " + str(self.getUser().getbalance())), anchor = "w")
        exitGameButton = Button(gameFrame, text = "EXIT", command = self.exitGame)
        playerNameLabel.grid(row = 0, column = 0)
        playerBalanceLabel.grid(row = 1, column = 0)
        #cardOneButton = button(gameFrame, image =
        #cardTwoButton = button(gameFrame, image =
        #cardThreeButton = button(gameFrame, image =
        #cardFourButton = button(gameFrame, image =
        #cardFiveButton = button(gameFrame, image =
        #cardDeckButton = button(gameFrame, image =
        #cardDeckButton.grid(row = 2, column = 0)
        #cardOneButton.grid(row = 2, column = 3)
        #cardTwoButton.grid(row = 2, column = 3)
        #cardThreeButton.grid(row = 2, column = 4)
        #cardFourButton.grid(row = 2, column = 5)
        #cardFiveButton.grid(row = 2, column = 6)
        exitGameButton.grid(row = 0, column = 100)
        gameFrame.grid(row = 0, column = 0)
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

    def readablehand(self, card):
        #Creates card ranks
        card_rank = [0: "2", 1: "3", 2: "4", 3: "5", 4: "6", 5: "7", 6: "8",
                     7: "9", 8: "10", 9: "J", 10: "Q", 11: "King", 12: "A"]
        #Creates card suits
        card_suit = [0: "Hearts", 1: "Diamonds", 2: "Clubs", 3: "Spades"]
        #Creates an empty return string
        return_string = ""
        #Creates a for loop that returns the card rank and card suit
        for i in cards:
            return_string += card_rank[i[0]] + card_suit[i[1]]
        return return_string

    def handcopy(self, card):
        #Creates an empty results list
        results = []
        #Creates a for loop that returns the hand of the player
        for i in cards:
            results.append(i)
        return results

    def numerichand(self, cards):
        # Converts alphanumeric hand to numeric values for easier comparisons
        # Also sorts cards based on rank
        card_rank = ["2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6,
                     "9": 7, "10": 8, "J": 9, "Q": 10, "K": 11, "A": 12,
                     "10": 8, "j": 9, "q": 10, "k": 11, "a": 12]
        card_suit = ["c": 0, "C": 0, "d": 1, "D": 1, "h": 2,
                     "s": 3, "S": 3, "H": 2]
        result = []
        for i in range(len(cards)// 2 + len(cards) % 2):
            result.append([card_rank[cards[i * 2]], card_suit[cards[i * 2 + 1]]])
        result.sort()
        result.reverse()
        return result

    def isFlush(self, hand):
        # Returns True if hand is a Flush, otherwise returns False
        hand_suit = [hand[0][1], hand[1][1], hand[2][1], hand[3][1], hand[4][1]]
        for i in range(4):
            if hand_suit.count(i) == 5:
                return True
        return False

    def isStraight(self, hand):
        # Return True if hand is a Straight, otherwise returns False
        if hand[0][0] == (hand[1][0] + 1) == (hand[2][0] + 2) == (hand[3][0] + 3) == (hand[4][0] + 4):
            return True
        elif (hand[0][0] == 12) and (hand[1][0] == 3) and (hand[2][0] == 2) and (hand[3][0] == 1) and (hand[4][0] == 0):
            return True
        return False

    def isStraightFlush(self, hand):
        # Return True if hand is a Straight Flush, otherwise returns False
        if check_flush(hand) and check_straight(hand):
            return True
        return False
        
        

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
