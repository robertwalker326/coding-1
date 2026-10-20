# loop- a loop is a conrtrast (special function) that repeats itself.
# In programming, a loop allows to repeat code instructions.

# there are two types of loops: for loop and while loop

# while loop- a type of loop where so long as a condition is qual
# to true it will keep running"forever"

# the keyword is while --> do while

# syntax
num = 4
while 2+2 == num: # condition --> operations - must be true
    print("the program is running...")
    mum= int(input("please type in any number but 4 to stop this program"))

# while loops will always run unless you change the condition!
# we can do this by writing instructions to manually change it.
# the computer must always complete their tasks before moving to the
# next step

def guessingGame():
    correctanswer= 8
    attempts= 0

    print("welcome to the guessing game")
    print("please type in a number between 1 and 10")

    userguess = int(input("please type in a number: "))
    while userguess != correctanswer:
        print("sorry,incorrect. guess again")
        attemp: = 1
        print(attempts)
        userguess= int(input("please try another number:"))
    print("congrats! you guessed correctly. game over ")

guessingame()