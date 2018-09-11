import random
import string

#Set guesses to nil
guesses = ""

'''
This function loads the set of puzzles into the program.
'''

def loadPuzzles(filename='wordblitzclues.txt'):
    fileClues = open(filename,'r')
    lisClues = []
    for line in fileClues:
        lisClues.append(line.rstrip()) #rstrip strips all chars from the end of the string.
    fileClues.close()
    return lisClues

'''
This function loads a random puzzle from the list of puzzles.
Removes any extra tabs that may be in the imported clue or word.
'''

def getRandomPuzzle(puzzleLis):
    randomIndex = random.randint(0, len(puzzleLis)-1)
    puzzle = puzzleLis[randomIndex].split('\t')
    for extraTab in puzzle:
        if extraTab == '':
            puzzle.remove('')
    
    hint = puzzle[0]
    word = puzzle[1]
    return hint,word

'''
Prints out 4 random puzzles at a time for demo purposes
'''

for i in range(4):
    puzzleLis = loadPuzzles() #Loads the puzzles into the program.
    hint,word = getRandomPuzzle(puzzleLis) #Selects a random puzzle

'''
Giving the user a choice between player vs player or player vs computer
'''
def gameChoice():
            
   
    a = int(input("\nWould you like to play with two players (1), or against the computer (2)? "))

    while a not in range(1,3):
        a = int(input("Invalid number! Please enter a number between 1 and 2!"))
       
    if a is 1:
        a = str(a)
        print("You chose " + a, ", you are playing against another player!")
        return 1
        
    else:
        a = str(a)
        print("You chose " + a, ", you are playing against the computer!")
        return 2 

#naming players/choosing if computer or not with the help of the gameChoice function
choice = gameChoice()

if choice is 1:
    playerOne = input("Player 1: What is your name?")
    playerTwo = input("Player 2: What is your name?")
    
else:
    playerOne = input("What is your name?")
    playerTwo = "Computer"
        
# function for if the user spins the wheel
def spinTheWheel(player):

    #generate random number within range
    spin = random.randint(0,21)

    return spin

#function to print the word
def printWord(word, guesses):
    
    emptySpace = 0
    word = word.lower()
    guesses = guesses.lower()
    for char in word:      
        if char in guesses:    
            print(char, end = "")   
        else:
            print(" _ ", end = "")

            

#function used to display menu including the clues, pla
def displayMenu(word, guesses, currentPlayer, hint):
    print("\nThe clue for this game is: " + hint)
    print("The secret word is: ", end = "")
    printWord(word, guesses)
    print("\nIt is " + currentPlayer, "'s turn! Choose an option")
    print("1: Spin the wheel?")
    print("2: Buy a vowel?")
    print("3: Guess the word?")
    print("4: Quit?")



#Receive a menu choice from the user
def menuChoice(menuSelection):
        
    if menuSelection is 1:
        return 1

    elif menuSelection is 2:
        return 2

    elif menuSelection is 3:
        return 3

    else:
        return 4

#helper function to the guessing functions to count word occurences
def countWord(word, guess):
    guess = word.count(guess)
    return guess

#consonant input for choice one in menu selection
def consonantInput(word, guesses, a):
   
    if a not in word:
        print("There was not a " + a, "in the word! ")
        return (0, guesses)

    elif a in word:
        guesses += a
        numOfOccurrences = 0
        numOfOccurrences = countWord(word, a)
        
        print("There was " + str(numOfOccurrences), " " + a, "'s in the word! ")
        return (numOfOccurrences, guesses)

#function to buy a vowel, purchasing and verifying input is done inside the control functions below

def buyVowel(word, guesses, b):

    b = b.lower()
    word = word.lower()
    guesses = guesses.lower()
    #check if the vowel is in the word or not
    if b not in word:
        print("There was not an " + b, "in the word! ")
        return (0, guesses)

    elif b in word:
        guesses += b       
        print("There was an " + b, " in the word! ")
        return (1, guesses)

    #function to guess the word straight, run by comparing the actual word to the input directly.
def guessTheWord(word, guesses):

    a = str(input("Please enter your word guess! "))
    a = a.lower()
    word = word.lower()
    guesses = guesses.lower()
    if a != word:
        print("Wrong!")
        return (0, guesses)
    else:
        print("You correctly guessed the word! ")
        guesses = a
        return (1, guesses)

    #winchecker is a function to determine IF there is a winner, this is used in conjunction with winCheckHelper to see WHO the winner is
def winChecker(word, guesses, playerOne, playerTwo, gBp1, gBp2):
    emptySpace = 0
    word = word.lower()
    guesses = guesses.lower()
   
    for char in word:      

        if char not in guesses: 
            emptySpace += 1
        else:
            #if there is no empty space, that means there is a winner
            emptySpace = 0

    if emptySpace is 0:
        return 0

    else: 
        return 1

#helper function as explained above, compares the balances of the two players and returns the winners name (or 0 if it is a tie)
def winCheckHelper(playerOne, playerTwo, gBp1, gBp2):
        
    if gBp1 > gBp2:
        return playerOne
    elif gBp1 < gBp2:
        return playerTwo
    else:
        return 0

    
#declaring all the global variables needed
turnCounter = 1
currentBalance = 0
turnBalanceP1 = 0
gameBalanceP1 = 0
turnBalanceP2 = 0
gameBalanceP2 = 0

#main function for player control. This is used for both players via turn counter which checks whos turn it is (1 is playerOne, 2 is playerTwo)
def playerControls(p1, p2, currentPlayer, turnCounter, guesses, word, currentBalance, tBp1, gBp1, tBp2, gBp2):
   
    print("\n" + playerOne, "'s Turn Balance: $" + str(tBp1), "   " +  playerTwo, "'s Game Balance: $" + str(tBp2))
    print("\n" + playerOne, "'s Game Balance: $" + str(gBp1), "   " +  playerTwo, "'s Game Balance: $" + str(gBp2))
    displayMenu(word, str(guesses), currentPlayer, hint)

    #menuChoice function input and verification
    menuSelection = input("\nWhat would you like to do?")
    menuSelection = int(menuSelection)

    while menuSelection not in range(1,5):
        menuSelection = input("Invalid number! Please enter a number between 1 and 4!")
        menuSelection = int(menuSelection)
    option = menuChoice(menuSelection) 

    consonantDollars = 0
        
    #if the user chooses the first option (spinning the wheel and guessing a consonant
    if option is 1:

        consonantDollars += spinTheWheel(currentPlayer)
            
        #if the spin results in 0, brankruptcy
        if consonantDollars is 0:
            print(currentPlayer, "spun a Bankruptcy Element! Next persons turn!")
            currentBalance = 0
            turnCounter += 1
            
            return (1, str(guesses), gBp1, gBp2, tBp1, tBp2, turnCounter)
                
                
        #if the spin results in 21, lose-a-turn
        elif consonantDollars is 21:
            print(currentPlayer, "spun a lose-a-turn element! Next persons turn!")
            currentBalance += consonantDollars

            if turnCounter is 1:
                gBp1 += currentBalance

            elif turnCounter is 2:
                gBp2 += currentBalance

            currentBalance = 0
            turnCounter += 1
           
            return (1, str(guesses), gBp1, gBp2, tBp1, tBp2, turnCounter)
        
        #if any other number, the number becomes the amount of dollars
        else:
            print(currentPlayer, "spun a " + str(consonantDollars))
            #verify that a consonant is inputted and hasnt already been guessed before
            vowels = "aeiou"
            print("Please pick a consonant")
            a = str(input())
            a = a.lower()
            word = word.lower()
            guesses = guesses.lower()
            while a in vowels or a in guesses:
                print("Please pick a consonant!")
                a = str(input())
            a = a.lower()

            menuInput, guesses = consonantInput(word, guesses, a)
             
            #if the consonant is wrongly guessed, their turn balance is deducted by the value of spin
            if menuInput is 0:
                currentBalance -= consonantDollars
                print(currentPlayer, "Loses $" + str(consonantDollars), "!")
                
                #if the turn is over set the TB to GB and TB becomes 0 depending on the turnCount which determines who the player was
                if turnCounter is 1:
                    tBp1 += currentBalance
                    gBp1 += tBp1
                    tBp1 = 0
                elif turnCounter is 2:
                    tBp2 += currentBalance
                    gBp2 = tBp2
                    tBp2 = 0
                
                turnCounter += 1
                currentBalance = 0
           
                return (1, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)

            #if the consonant is correct, their turn balance is increased by the value of spin
            else:
                currentBalance += consonantDollars
                print(playerOne, "Wins $" + str(currentBalance), "!")

                if turnCounter is 1:
                    tBp1 += (menuInput * currentBalance)

                elif turnCounter is 2:
                    tBp2 += (menuInput * currentBalance)

                currentBalance = 0

                #using the winChecker and winCheckHelper function to determine if and who the winner is
                winCheck = winChecker(word, guesses, playerOne, playerTwo, gBp1, gBp2)

                if winCheck is 0:
                    print("It's a tie!")
                    return (0, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)
                else:
                    print(winCheckHelper(playerOne, playerTwo, gBp1, gBp2), "won the game!")
                    return (0, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)

        return (1, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)


    elif option is 2:
        #buying the vowel is -25$
        currentBalance -= 25

        #vowel verification and input
        vowels = "aeiou"
        print("Please pick a vowel")
        b = str(input())
        while b not in vowels or b in guesses:
            print("Please pick a vowel!")
            b = str(input())

        menuInput, guesses = buyVowel(word, guesses, b)

        if menuInput is 0:
            print("\nIt is now the next players turn!")
            
            #turn change as explained above
            if turnCounter is 1:
                tBp1 += currentBalance
                gBp1 += tBp1
                tBp1 = 0

            elif turnCounter is 2:
                tBp2 += currentBalance
                gBp2 = tBp2
                tBp2 = 0      
            
            currentBalance = 0
            turnCounter += 1

        else:

            if turnCounter is 1:
                tBp1 += currentBalance

            elif turnCounter is 2:
                tBp2 += currentBalance

                #win check as explained above
            winCheck = winChecker(word, guesses, playerOne, playerTwo, gBp1, gBp2)

            if winCheck is 0:
                if turnCounter is 1:
                    tBp1 += currentBalance
                    gBp1 += tBp1
                    tBp1 = 0

                elif turnCounter is 2:
                    tBp2 += currentBalance
                    gBp2 = tBp2
                    tBp2 = 0     

                winCheck = winCheckHelper(playerOne, playerTwo, gBp1, gBp2)
                if winCheck is 0:
                    print("It's a tie!")
                    return (0, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)
                else:
                    print(winCheckHelper(playerOne, playerTwo, gBp1, gBp2), "won the game!")
                    return (0, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)
            else:
                return (1, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)
        return (1, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)

    elif option is 3:
        menuInput, guesses = guessTheWord(word, guesses)

        if menuInput is 0:
            print("\nIt is now the next players turn!")

            if turnCounter is 1:
                tBp1 += currentBalance
                gBp1 += tBp1
                tBp1 = 0

            elif turnCounter is 2:
                tBp2 += currentBalance
                gBp2 = tBp2
                tBp2 = 0      
            
            currentBalance = 0
            turnCounter += 1

        else:
            print("The correct word was: " + guesses, "!")

            if turnCounter is 1:
                tBp1 += currentBalance
                gBp1 += tBp1
                tBp1 = 0

            elif turnCounter is 2:
                tBp2 += currentBalance
                gBp2 = tBp2
                tBp2 = 0 

            winCheck = winCheckHelper(playerOne, playerTwo, gBp1, gBp2)
            if winCheck is 0:
                print("It's a tie!")
                return (0, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)
            else:

                print(winCheckHelper(playerOne, playerTwo, gBp1, gBp2), "won the game!")
                return (0, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)   
        return (1, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)

    else:
        winChecker(word, guesses, playerOne, playerTwo, gBp1, gBp2)
        print("Goodbye!")
        return (0, str(guesses), gBp1, gBp2, tBp1, tBp2, turnCounter)



    #computer controlled function, this is done by creating randomly generated numbers and letters in order to play the game
def computerControls(p1, p2, currentPlayer, turnCounter, guesses, word, currentBalance, tBp1, gBp1, tBp2, gBp2):

    print("\n" + playerOne, "'s Turn Balance: $" + str(tBp1), "   " +  playerTwo, "'s Game Balance: $" + str(tBp2))
    print("\n" + playerOne, "'s Game Balance: $" + str(gBp1), "   " +  playerTwo, "'s Game Balance: $" + str(gBp2))
    displayMenu(word, str(guesses), currentPlayer, hint)

    
    print("\nComputer, what would you like to do?")
    menuSelection = random.randint(1,3)
    menuSelection = int(menuSelection)

    while menuSelection is 3:

        menuSelection = random.randint(1,3)
        menuSelection = int(menuSelection)
    print("The computer has chosen " + str(menuSelection), "!")
    option = menuChoice(menuSelection) 

    consonantDollars = 0
        
    #if the user chooses the first option (spinning the wheel and guessing a consonant
    if option is 1:

        consonantDollars += spinTheWheel(currentPlayer)
            
        #if the spin results in 0, brankruptcy
        if consonantDollars is 0:
            print(currentPlayer, "spun a Bankruptcy Element! Next persons turn!")
            currentBalance = 0
            turnCounter += 1
            
            return (1, str(guesses), gBp1, gBp2, tBp1, tBp2, turnCounter)
                
                
        #if the spin results in 21, lose-a-turn
        elif consonantDollars is 21:
            print(currentPlayer, "spun a lose-a-turn element! Next persons turn!")
            currentBalance = 0

            if turnCounter is 1:
                gBp1 += currentBalance

            elif turnCounter is 2:
                gBp2 += currentBalance

            currentBalance = 0
            turnCounter += 1
           
            return (1, str(guesses), gBp1, gBp2, tBp1, tBp2, turnCounter)
        
        #if any other number, the number becomes the amount of dollars
        else:
            print(currentPlayer, "spun a " + str(consonantDollars))
            
            vowels = "aeiou"
            a = random.choice(string.ascii_letters)
            a = a.lower()
            word = word.lower()
            guesses = guesses.lower()

            while a in vowels or a in guesses:
                a = random.choice(string.ascii_letters)
                a = str(input())
            a = a.lower()

            menuInput, guesses = consonantInput(word, guesses, a)
             
            #if the consonant is wrongly guessed, their turn balance is deducted by the value of spin
            if menuInput is 0:
                currentBalance -= consonantDollars
                print(currentPlayer, "Loses $" + str(consonantDollars), "!")
                
                if turnCounter is 1:
                    tBp1 += currentBalance
                    gBp1 += tBp1
                    tBp1 = 0
                elif turnCounter is 2:
                    tBp2 += currentBalance
                    gBp2 = tBp2
                    tBp2 = 0
                
                turnCounter += 1
                currentBalance = 0
           
                return (1, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)

            #if the consonant is correct, their turn balance is increased by the value of spin
            else:
                currentBalance += consonantDollars
                print(playerOne, "Wins $" + str(currentBalance), "!")

                if turnCounter is 1:
                    tBp1 += (menuInput * currentBalance)

                elif turnCounter is 2:
                    tBp2 += (menuInput * currentBalance)

                currentBalance = 0

                winCheck = winChecker(word, guesses, playerOne, playerTwo, gBp1, gBp2)

                if winCheck is 0:
                    print(winCheckHelper(playerOne, playerTwo, gBp1, gBp2))
                    return (0, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)
                else:
                    return (1, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)
        return (1, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)


    elif option is 2:
        currentBalance -= 25

        vowels = "aeiou"
        
        #random letter input and verification
        b = random.choice(string.ascii_letters)
        while b not in vowels or b in guesses:
            b = random.choice(string.ascii_letters)

        menuInput, guesses = buyVowel(word, guesses, b)

        if menuInput is 0:
            print("\nIt is now the next players turn!")
            
            if turnCounter is 1:
                tBp1 += currentBalance
                gBp1 += tBp1
                tBp1 = 0

            elif turnCounter is 2:
                tBp2 += currentBalance
                gBp2 = tBp2
                tBp2 = 0      
            
            currentBalance = 0
            turnCounter += 1

        else:

            if turnCounter is 1:
                tBp1 += currentBalance

            elif turnCounter is 2:
                tBp2 += currentBalance

            winCheck = winChecker(word, guesses, playerOne, playerTwo, gBp1, gBp2)

            if winCheck is 0:
                if turnCounter is 1:
                    tBp1 += currentBalance
                    gBp1 += tBp1
                    tBp1 = 0

                elif turnCounter is 2:
                    tBp2 += currentBalance
                    gBp2 = tBp2
                    tBp2 = 0     

                    #win check code again
                winCheck = winCheckHelper(playerOne, playerTwo, gBp1, gBp2)
                if winCheck is 0:
                    print("It's a tie!")
                    return (0, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)
                else:
                    print(winCheckHelper(playerOne, playerTwo, gBp1, gBp2), "won the game!")
                    return (0, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)
            else:
                return (1, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)
        return (1, guesses, gBp1, gBp2, tBp1, tBp2, turnCounter)

    
    else:
        winChecker(word, guesses, playerOne, playerTwo, gBp1, gBp2)
        print("Goodbye!")
        return (0, str(guesses), gBp1, gBp2, tBp1, tBp2, turnCounter)

#MAIN CODE this is used to run the above functions
while True:

    #if player ones turn, run the player control function with the current player as playerOne
    if turnCounter is 1:
        quit, guesses, gameBalanceP1, gameBalanceP2, turnBalanceP1, turnBalanceP2, turnCounter = playerControls(playerOne, playerTwo, playerOne, turnCounter, guesses, word, currentBalance, turnBalanceP1, gameBalanceP1, turnBalanceP2, gameBalanceP2)

        #if the user chooses option 4 it will break the loop and end the program
        if quit is 0:
            break

    #if player twos turn, run the player control function with the current player as playertwo
    elif turnCounter is 2 and choice is 1:
        quit, guesses, gameBalanceP1, gameBalanceP2, turnBalanceP1, turnBalanceP2, turnCounter = playerControls(playerOne, playerTwo, playerTwo, turnCounter, guesses, word, currentBalance, turnBalanceP1, gameBalanceP1, turnBalanceP2, gameBalanceP2)

        if quit is 0:
            break

    
    #computer control function just as above
    elif turnCounter is 2 and choice is 2:
        quit, guesses, gameBalanceP1, gameBalanceP2, turnBalanceP1, turnBalanceP2, turnCounter = computerControls(playerOne, playerTwo, playerTwo, turnCounter, guesses, word, currentBalance, turnBalanceP1, gameBalanceP1, turnBalanceP2, gameBalanceP2)
        
        if quit is 0:
            break
    #if the turn counter is 3, set it to 1 so it goes from 1 -> 2 -> 1 infinitly 
    else:
        turnCounter = 1






        
