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





# Question 1
# password reset function. Your function should take in a 
# user password as an input.within the function there should be a 
# variable that contains the correct password.
# the user should be able to attempt to enter the password 4 times. 
# On the fourth attempt of getting the password inccorect, 
# it should print out a message telling the user that 
# their account has been locked. If the user gets the password 
# correct it should print out a message telling them 
# they can access their account.



# Question 2
# Create a shots made-to-attempts function. your function should prompt the user to enter if they
# made or missed a shot. If they enter made, it will give the user 2 points. else if they miss it 
# will not give them points. Every shot must be recorded. If your user enters the letter "q", it 
# will show how many points they made as well as the number of attempts they've made


def password_reset():
    correct_password = "SecretPassword123"
    max_attempts = 4
    attempts = 0

    print("welcome to password reset")
    print("please type in a number")


    for in range(attempts):
            user_input = input("Enter your password: ")
    user_input == correct_password:
    print("You can access your account.")
    return

    
 for attempt in range(max_attempts):
        user_input = input("Enter your password: ")

        if user_input == correct_password:
            print("You can access your account.")
             return

        print("Your account has been locked.")




def shots_made_to_attempts():
        points = 0
        attempts = 0
            
while True:
        result= input("Enter 'made' or 'missed' (or 'q' to finish): ").strip().lower()
        
        if result == "q":
            print(f"Points: {points}; attempts: {attempts}")
            break
            
            
while True:
        if result in ("made", "missed"):
            attempts += 1
            if result == "made":
                points += 2
        else:
            print("Please enter 'made', 'missed', or 'q'.")