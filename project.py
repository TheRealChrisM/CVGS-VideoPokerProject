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

class Card():

    ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    suits = ('S', 'D', 'H', 'C')

    def __init__ (self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__ (self):
        if self.rank == 14:
          rank = 'A'
        elif self.rank == 13:
          rank = 'K'
        elif self.rank == 12:
          rank = 'Q'
        elif self.rank == 11:
          rank = 'J'
        else:
          rank = self.rank
        return str(rank) + self.suit


#create game class
class Game:
    #Constructs the Game Object with an input of a list of users.
    def __init__(self, userList):
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
        self.userLogin()
        return
    
    def setUser(self, curUser):
        self.__currentUser = curUser
        return

    def getUser(self):
        return self.__currentUser

    def play(self):
        for i in range(len(self.cardDeck) ):
          sortedHand = sorted (self.cardDeck[i], reverse = True)
          hand = ''
          for card in sortedHand:
            hand = hand + str(card) + ' '
          print ('Hand ' + str(i + 1) + ': ' + hand)

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
        loginFrame.pack_forget()
        #Creates the title of the window as "Video Game Poker"
        window.title("Video Game Poker")
        playerNameLabel = Label(gameFrame, text = (self.getUser().getfirstname() + " " + self.getUser().getlastname()), anchor = "w")
        playerBalanceLabel = Label(gameFrame, text = ("Balance: " + str(self.getUser().getbalance())), anchor = "w")
        #Creates a button that exits the game
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
        window.destroy()  #Exits and destroys the window 
        return
    
    def checkPassword(self):
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
        sortedHand = sorted(hand,reverse=True)
        card_sum = 0 #Initializes the card sum
        ranklist = [] #Creates an empty list that stores the card rank
        for card in sortedHand:
          ranklist.append(card.rank) #Adds the card rank to the empty list that stores rank
        card_sum = ranklist[0]*13**4+ranklist[1]*13**3+ranklist[2]*13**2+ranklist[3]*13+ranklist[4] #Creates value of the card sum
        return card_sum #Returns the card sum

    def isRoyalFlush(self, hand):                
        sortedHand=sorted(hand,reverse=True)
        flag=True #Creates a variable that stores a Boolean value
        h=10
        Currentsuit=sortedHand[0].suit 
        Currentrank=14
        total_point=h*13**5+self.point(sortedHand)
        for card in sortedHand:
          if card.suit!=Currentsuit or card.rank!=Currentrank:
            flag=False
            break
          else:
            Currentrank-=1
        if flag:
            print('Royal Flush') #returns the total_point and prints out 'Royal Flush' if true
            self.tlist.append(total_point) #Adds the total amount of points to the empty list   
        else:
          self.isStraightFlush(sortedHand) #if false, pass down to isStraightFlush(hand)


    def isStraightFlush(self, hand):        
        sortedHand=sorted(hand,reverse=True)
        flag=True #Creates a variable that stores a Boolean value
        h=9
        Currentsuit=sortedHand[0].suit
        Currentrank=sortedHand[0].rank
        total_point=h*13**5+self.point(sortedHand)
        for card in sortedHand:
          if card.suit!=Currentsuit or card.rank!=Currentrank:
            flag=False
            break
          else:
            Currentrank-=1
        if flag:
          print ('Straight Flush') #returns the total_point and prints out 'Straight Flush' if true
          self.tlist.append(total_point) #Adds the total amount of points to the empty list 
        else:
          self.isFour(sortedHand) #if false, pass down to isFour(hand)

    def isFourOfAKind(self, hand):                  #returns the total_point and prints out 'Four of a Kind' if true, if false, pass down to isFull()
        sortedHand=sorted(hand,reverse=True)
        flag=True #Creates a variable that stores a Boolean value
        h=8
        Currank=sortedHand[1].rank               #since it has 4 identical ranks,the 2nd one in the sorted listmust be the identical rank
        count=0
        total_point=h*13**5+self.point(sortedHand)
        for card in sortedHand:
          if card.rank==Currank:
            count+=1
        if not count<4:
          flag=True
          print('Four of a Kind')
          self.tlist.append(total_point)#Adds the total amount of points to the empty list  

        else:
          self.isFull(sortedHand)

    def isFullHouse(self, hand):                      
        sortedHand=sorted(hand,reverse=True)
        flag=True #Creates a variable that stores a Boolean value
        h=7
        total_point=h*13**5+self.point(sortedHand)
        mylist=[]  #create a list to store ranks
        for card in sortedHand:
          mylist.append(card.rank)
        rank1=sortedHand[0].rank #The 1st rank and the last rank should be different in a sorted list
        rank2=sortedHand[-1].rank
        num_rank1= mylist.count(rank1)
        num_rank2= mylist.count(rank2)
        if (num_rank1==2 and num_rank2==3)or (num_rank1==3 and num_rank2==2):
          flag=True
          print ('Full House') #returns the total_point and prints out 'Full House' if true
          self.tlist.append(total_point) #Adds the total amount of points to the empty list 
          
        else:
          flag=False #Creates a variable that creates a False Boolean value
          self.isFlush(sortedHand) #if false, pass down to isFlush()

    def isFlush(self, hand):                          
        sortedHand=sorted(hand,reverse=True)
        flag=True #Creates a variable that stores a Boolean value
        h=6
        total_point=h*13**5+self.point(sortedHand)
        Cursuit=sortedHand[0].suit
        for card in sortedHand:
          if not(card.suit==Cursuit):
            flag=False
            break
        if flag:
          print ('Flush') #returns the total_point and prints out 'Flush' if true
          self.tlist.append(total_point) #Adds the total amount of points to the empty list 
          
        else:
          self.isStraight(sortedHand) #if false, pass down to isStraight()

    def isStraight(self, hand):
        sortedHand=sorted(hand,reverse=True)
        flag=True #Creates a variable that stores a Boolean value
        h=5
        total_point=h*13**5+self.point(sortedHand)
        Currank=sortedHand[0].rank  #this should be the highest rank
        for card in sortedHand:
          if card.rank!=Currank:
            flag=False
            break
          else:
            Currank-=1
        if flag:
          print('Straight')
          self.tlist.append(total_point) #Adds the total amount of points to the empty list 
          
        else:
          self.isThree(sortedHand)
        
    def isThreeOfAKind(self, hand):
        sortedHand=sorted(hand,reverse=True)
        flag=True #Creates a variable that stores a Boolean value
        h=4
        total_point=h*13**5+self.point(sortedHand)
        Currank=sortedHand[2].rank #In a sorted rank, the middle one should have 3 counts if flag=True
        mylist=[]
        for card in sortedHand:
          mylist.append(card.rank)
        if mylist.count(Currank)==3:
          flag=True
          print ("Three of a Kind")
          self.tlist.append(total_point) #Adds the total amount of points to the empty list 
          
        else:
          flag=False
          self.isTwo(sortedHand)
        
    def isTwoPair(self, hand): 
        sortedHand=sorted(hand,reverse=True)
        flag=True #Creates a variable that stores a Boolean value
        h=3
        total_point=h*13**5+self.point(sortedHand)
        rank1=sortedHand[1].rank #Rank of the 2nd card
        rank2=sortedHand[3].rank #Rank of the 4th card
        mylist=[] #create an empty list to store ranks
        for card in sortedHand:
          mylist.append(card.rank)
        if mylist.count(rank1)==2 and mylist.count(rank2)==2: #in a five cards sorted group, if isTwo(), the 2nd and 4th card should have another identical rank
          flag=True
          print ("Two Pair") #returns the total_point and prints out 'Two Pair' if true, 
          self.tlist.append(total_point) #Adds the total amount of points to the empty list 
          
        else:
          flag=False
          self.isOne(sortedHand) #if false, pass down to isOne()

    def isJacks(self, hand):                           
        sortedHand=sorted(hand,reverse=True)
        flag=True
        h=2
        total_point=h*13**5+self.point(sortedHand)
        mylist=[] #create an empty list to store ranks
        mycount=[] #create an empty list to store number of count of each rank
        for card in sortedHand:
          mylist.append(card.rank) #Adds a sorted card to the empty list
        for each in mylist:
          count=mylist.count(each)
          mycount.append(count)
        if mycount.count(2)==2 and mycount.count(1)==3:  #There should be only 2 identical numbers and the rest are all different
          flag=True
          print ("One Pair")#returns the total_point and prints out 'One Pair' if true
          self.tlist.append(total_point) #Adds the total amount of points to the empty list 
          
        else:
          flag=False
          self.isHigh(sortedHand) #if false, pass down to isHigh()


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

    def endgame(self):
        #Creates a Button that shows what each team member contributed
        teamButton = Button(gameFrame, text = "Click to show which team member did what", command = teammember)

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
