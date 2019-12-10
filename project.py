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
#Stores the user's desired recovery question for registration
recoveryQuestion = StringVar()
#Stores the user's desired recovery answer for registration
recoveryAnswer = StringVar()
#Stores the user's first name for registration
firstName = StringVar()
#stores the user's last name for registration
lastName = StringVar()
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


class Card(): #Creates a class for the card deck
    
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] #Creates a list for the card ranks
    suits = ['S', 'D', 'H', 'C'] #Creates a list for the card suits

    def __init__ (self, rank, suit):
        self.rank = rank #Creates an initialized variable for the card ranks
        self.suit = suit #Creates an initialized variable for the card suits

    def __str__ (self):
        if self.rank == 14:
          rank = 'A' #Returns as an Ace if the card rank is 14
        elif self.rank == 13:
          rank = 'K' #Returns as a King if the card rank is 13
        elif self.rank == 12:
          rank = 'Q' #Returns as a Queen if the card rank is 12
        elif self.rank == 11:
          rank = 'J' #Returns as a Jack if the card rank is 11
        else:
          rank = self.rank #Otherwise, it returns the rank's number
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
        #Moves to the function which allows a user to login.
        self.__userHand = [0,0,0,0,0]
        self.__userHandImage = ["","","","",""]
        self.userLogin()
        return
    
    def setUser(self, curUser):
        self.__currentUser = curUser #Creates a variable for the current user
        return

    def getHand(self, index):
        return self.__userHand[index]
    
    def getUser(self):
        return self.__currentUser #Fetches the current user

    def setUserHandImage(self, index, imageNum):
        self.__userHandImage[index] = ImageTk.PhotoImage(file="card/"+str(self.getcard(imageNum))+".gif")
        return

    def getUserHandImage(self, index):
        return self.__userHandImage[index]
    
    #Creates a function that draws a random card
    def newcard(self):
        randomCard = random.randint(0,51) #Creates a random card from 0 to 51
        while (self.drawn(randomCard)):
           randomCard = random.randint(0,51)
        self.setDrawn(randomCard)
        return (randomCard + 1)

    #Adds new cards to a player's hand
    def addcard(self, cardIndex):
        self.__userHand[cardIndex] = self.newcard()
        return

    def play(self):
        for i in range(len(self.cardDeck) ):
          sortedHand = sorted (self.cardDeck[i], reverse = True)
          hand = ''
          for card in sortedHand:
            hand = hand + str(card) + ' '
          print ('Hand ' + str(i + 1) + ': ' + hand)

    #Creates a function that draws a random card and adds it to the deck 
    def newcard():
        
        return newcard


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

<<<<<<< HEAD
=======
    def registerUser(self):
        global recoveryQuestion, recoveryAnswer, firstName, lastName
        loginFrame.pack_forget()
        firstNameLabel = Label(registerFrame, text = "First: ")
        firstNameEntry = Entry(registerFrame, textvariable = firstName)
        lastNameLabel = Label(registerFrame, text = "Last: ")
        lastNameEntry = Entry(registerFrame, textvariable = lastName)
        newUserLabel = Label(registerFrame, text = "Please enter a password recovery question.")
        passwordRecoveryEntry = Entry(registerFrame, textvariable = recoveryQuestion)
        passwordRecoveryAnswerLabel = Label(registerFrame, text = "What is the answer to this question?")
        passwordRecoveryAnswerEntry = Entry(registerFrame, textvariable = recoveryAnswer)
        registerSubmitButton = Button(registerFrame, text = "SUBMIT", command = self.submitRegistration)
        firstNameLabel.grid(row = 0, column = 0)
        firstNameEntry.grid(row = 0, column = 1)
        lastNameLabel.grid(row = 1, column = 0)
        lastNameEntry.grid(row = 1, column = 1)
        newUserLabel.grid(row = 2, columnspan = 2)
        passwordRecoveryEntry.grid(row = 3, columnspan = 2)
        passwordRecoveryAnswerLabel.grid(row = 4, columnspan = 2)
        passwordRecoveryAnswerEntry.grid(row = 5, columnspan = 2)
        registerSubmitButton.grid(row = 6, columnspan = 2)
        registerFrame.pack()
        return

    def submitRegistration(self):
        newFirstName = firstName.get()
        newLastName = lastName.get()
        newUsername = username.get()
        newPassword = password.get()
        newRecoveryQuestion = recoveryQuestion.get()
        newRecoveryAnswer = recoveryAnswer.get()
        newUser = Player(newFirstName, newLastName, newUsername, newPassword, newRecoveryQuestion, newRecoveryAnswer)
        print(newFirstName, newLastName, newUsername, newPassword, newRecoveryQuestion, newRecoveryAnswer)
        self.addUser(newUser)
        messagebox.showinfo("New User", (firstName.get() + ", you have successfully registered! \n Please log in!"))
        registerFrame.pack_forget()
        self.userLogin()
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
        print(self.__users)
        print(selectedUser)
        print(savedUser.getpassword().get())
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
        correctPassword = savedUser.getpassword()
        passwordHintPromptText = savedUser.getpasswordhintQuestion()
        passwordHintPromptLabel = Label(forgotPasswordFrame, text = passwordHintPromptText, wraplength = 250, justify = LEFT, pady = 5)
        passwordHintEntry = Entry(forgotPasswordFrame, textvariable = forgotPasswordInput)
        passwordHintButton = Button(forgotPasswordFrame, text = "SUBMIT", command = self.checkPasswordHint)
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
            #Creates a message box if the ser gives an incorrect response to the password hint 
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
        cardDeckButton.grid(row = 2, column = 0, padx = 50) #Grids the Card Deck Button
        cardOneButton.grid(row = 2, column = 1, padx = 5) #Grids the Card One Button
        cardTwoButton.grid(row = 2, column = 2, padx = 5) #Grids the Card Two Button
        cardThreeButton.grid(row = 2, column = 3, padx = 5) #Grids the Card Three Button
        cardFourButton.grid(row = 2, column = 4, padx = 5) #Grids the Card Four Button
        cardFiveButton.grid(row = 2, column = 5, padx = 5) #Grids the Card Five Button

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

    def point(self,hand): #point()function to calculate partial score
        sortedHand = sorted(hand, reverse = True) #Sorts the cards in the empty hand list
        card_sum = 0 #Initializes the card sum
        ranklist = [] #Creates an empty list that stores the card rank
        for card in sortedHand: #For each card in the sorted list 
          ranklist.append(card.rank) #Adds the card rank to the empty list that stores rank
        card_sum = ranklist[0]*13**4+ranklist[1]*13**3+ranklist[2]*13**2+ranklist[3]*13+ranklist[4] #Creates value of the card sum
        return card_sum #Returns the card sum

    def isRoyalFlush(self, hand): #Creates a function if the user has a Royal Flush          
        sortedHand = sorted(hand,reverse = True) #Sorts the cards in the empty hand list
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
        if flag:
            print('Royal Flush') #returns the total_point and prints out 'Royal Flush' if true
            self.tlist.append(total_point) #Adds the total amount of points to the empty list   
        else:
          self.isStraightFlush(sortedHand) #if false, pass down to isStraightFlush(hand)


    def isStraightFlush(self, hand): #Creates a function if the user has a Straight Flush     
        sortedHand = sorted(hand,reverse = True) #Sorts the cards in the empty hand list
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
        if flag: #If true
          print('Straight Flush') #returns the total_point and prints out 'Straight Flush' if true
          self.tlist.append(total_point) #Adds the total amount of points to the empty list 
        else:
          self.isFourOfAKind(sortedHand) #if false, pass down to isFour(hand)

    def isFourOfAKind(self, hand): #Creates a function if the user has four of a kind             
        sortedHand = sorted(hand,reverse = True) #Sorts the cards in the empty hand list
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
          print('Four of a Kind') #returns the total_point and prints out 'Four of a Kind' if true
          self.tlist.append(total_point)#Adds the total amount of points to the empty list  

        else:
          self.isFullHouse(sortedHand)#if false, pass down to isFull() 

    def isFullHouse(self, hand): #Creates a function if the user has a Full House                   
        sortedHand = sorted(hand,reverse = True) #Sorts the cards in the empty hand list
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
          print('Full House') #returns the total_point and prints out 'Full House' if true
          self.tlist.append(total_point) #Adds the total amount of points to the empty list 
          
        else:
          flag=False #Creates a variable that creates a False Boolean value
          self.isFlush(sortedHand) #if false, pass down to isFlush()

    def isFlush(self, hand): #Creates a function if the user has a Flush                     
        sortedHand=sorted(hand,reverse=True) #Sorts the cards in the empty hand list
        flag=True #Creates a variable that stores a Boolean value
        h = 6 #Stores an integer value
        total_point=h*13**5+self.point(sortedHand) #Returns the total points
        Currentsuit=sortedHand[0].suit #Returns the current suit of the card
        for card in sortedHand: #For each card in the sorted list 
          if not(card.suit == Currentsuit): #If card suit is not equal to the current suit
            flag=False #Return False
            break
        if flag: #Returns true
          print('Flush') #returns the total_point and prints out 'Flush' if true
          self.tlist.append(total_point) #Adds the total amount of points to the empty list 
          
        else:
          self.isStraight(sortedHand) #if false, pass down to isStraight()

    def isStraight(self, hand): #Creates a function if the user has a straight
        sortedHand = sorted(hand, reverse = True) #Sorts the cards in the empty hand list
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
          print('Straight') #Print Straight
          self.tlist.append(total_point) #Adds the total amount of points to the empty list 
          
        else:
          self.isThreeOfAKind(sortedHand)#if false, pass down to isThreeOfAKind(hand)
        
    def isThreeOfAKind(self, hand): #Creates a function if the user has three of a kind
        sortedHand = sorted(hand,reverse=True) #Sorts the cards in the empty hand list
        flag = True #Creates a variable that stores a Boolean value
        h = 4 #Stores an integer value
        total_point = h*13**5+self.point(sortedHand) #Returns the total points
        Currentrank = sortedHand[2].rank #In a sorted rank, the middle one should have 3 counts if flag=True
        mylist = [] #create a list to store ranks
        for card in sortedHand: #For each card in the sorted list 
          mylist.append(card.rank) #Adds the card rank to the empty mylist
        if mylist.count(Currentrank)== 3: #If the current rank in mylist is equal to 3
          flag = True #Returns true
          print ("Three of a Kind") #Print three of a kind
          self.tlist.append(total_point) #Adds the total amount of points to the empty list 
          
        else:
          flag=False #Return false
          self.isTwoPair(sortedHand) #if false, pass down to isTwoPair(hand)
        
    def isTwoPair(self, hand): #Creates a function if the user has a TwoPair
        sortedHand = sorted(hand,reverse=True) #Sorts the cards in the empty hand list 
        flag = True #Creates a variable that stores a Boolean value
        h=3 #Stores an integer value
        total_point=h*13**5+self.point(sortedHand) #Returns the total points
        rank1=sortedHand[1].rank #Rank of the 2nd card
        rank2=sortedHand[3].rank #Rank of the 4th card
        mylist=[] #create an empty list to store ranks
        for card in sortedHand: #For each card in the sorted list 
          mylist.append(card.rank) #Adds the card rank to the empty mylist
        if mylist.count(rank1)== 2 and mylist.count(rank2)== 2: #in a five cards sorted group, if isTwo(), the 2nd and 4th card should have another identical rank
          flag=True #Returns true
          print ("Two Pair") #returns the total_point and prints out 'Two Pair' if true, 
          self.tlist.append(total_point) #Adds the total amount of points to the empty list 
          
        else:
          flag=False
          self.isJacks(sortedHand) #if false, pass down to isJacks(hand)

    def isJacks(self, hand):#Creates a function if the user has Jacks                            
        sortedHand = sorted(hand, reverse = True) #Sorts the cards in the empty hand list
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
          print("One Pair")#returns the total_point and prints out 'One Pair' if true
          self.tlist.append(total_point) #Adds the total amount of points to the empty list 
          
        else:
          flag = False #Return false
 

    def getScore(self):
        score = 0 #Initializes the scores
        if self.isRoyalFlush(): #Returns a score of 250 if it is a Royal Flush
            score = 250
        elif self.isStraightFlush(): #Returns a score of 50 if it is a Straight Flush
            score = 50
        elif self.isFourOfAKind(): #Returns a score of 25 if it is Four of a Kind
            score = 25
        elif self.isFullHouse(): #Returns a score of 9 if it is a Full House
            score = 9
        elif self.isFlush(): #Returns a score of 6 if it is a Flush
            score = 6
        elif self.isStraight(): #Returns a score of 4 if it is a Straight
            score = 4
        elif self.isThreeOfAKind(): #Returns a score of 3 if it is Three of a Kind
            score = 3
        elif self.isTwoPair(): #Returns a score of 2 if it is a Two Pair
            score = 2
        elif self.isJacks(): #Returns a score of a 1 if it is a Jacks
            score = 1
        else:
            score = 0 #Otherwise the score is 0 
        return score

    def betButton(self): #Creates a function for creating a betting button
        betButton = Button(gameFrame, text = "PLACE YOUR BET", command) #Creates a button that allows the user to place their bet
        betButton.grid(row)


    def endgame(self):
        #Creates a Button that shows what each team member contributed
        teamButton = Button(gameFrame, text = "Click to show which team member did what", command = teammember)
        teamButton.grid(row) 

    def teammember(self):
        #Prints what each team member contributed
        print("William did the user class, card game logic such as Royal Flush, Straight Flush etc. while Chris did the user Login and password and gameplay")



#Add default users
userList.append(Player("King", "Howard", "kh", "cvgs", "Is Computer Science a real Science?", "True"))
userList.append(Player("Mickey", "Mouse", "mmouse", "Disney", "Where I work.", "Disney"))
userList.append(Player("John", "Doe", "jd", "bruh", "This is a test to see how long you can make password hints before things start getting weird so that we don't loose points for super duper long password hints.", "bruh"))
game = Game(userList)

#Starts the program
window.mainloop()
