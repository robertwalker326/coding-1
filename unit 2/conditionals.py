# Conditional if/else logic- these are keywords that instruct your
# program to do specific instructions based on specific data
# or conditions

# conditional syntax(how it is written)
bill_amount = int(input("please type in a bill tender( 1s,5s, or 10s):"))

# if usually indicates that something is a possible option
if bill_amount == 1:
    print("Here are 4 quarters")
# elif aloows us to indicate that there are more possible options
# you can have as many elif as you want
elif bill_amount == 5:
    print("here are 20 quarters")
elif bill_amount == 10:
    print("here are 40 quarters")
elif bill_amount == 20:
    print("sorry we dont accept 20s.")
# else is always your last option.
else:
    print("sorry that type of bill is not accpeted.")


def college():
    grade= int(input("please type in your grade."))
    if grade > 90:
        templeU()
    else:
        ccp():

    def templeU():
        print("congrats you meet the requirement for temple u")
        print("238293")

    def ccp():
        print("it looks like your gpa does not meet the requirement but you can apply yo ccp code")
        print("a7ds78sd")

    college()




    # using the calaulator functions from the calculator.py file,
    # create a main calculator function that uses if/else logic to
    # allow the user to select different artithmetic:operations and
    # then perform those operations by running their respective functions.

    # example:an input where if the user enter 1, it will run the addition functions.
    # 1= addition()
    # 2= subtraction()
    # 3= multiplication()
    # 4= division()

def calculate_add():
    print("program has started: please type in 2 numbers to add ")
    num1 = int(input())
    num2 = int(input())
    print(num1 + num2)
    print("program has ended. ")

def calculate_subtract():
    print("program has started: please type in 2 numbers to subtract ")
    num1 = int(input())
    num2 = int(input())
    print(num1 - num2)
    print("program has ended. ")

 def calculate_multiply():
    print("program has started: please type in 2 numbers to multiply ")
    num1 = int(input())
    num2 = int(input())
    print(num1 * num2)
    print("program has ended. ")


def calculate_division():
    print("program has started: please type in 2 numbers to divison ")
    num1 = int(input())
    num2 = int(input())
    print(num1 / num2)
    print("program has ended. ")

def maincalculator():
    selection = input()
    if(selection == 1):
        calculate_add()
    elif selection = 2:
        calculate_subtract()
    elif selection= 3:
         calculate_multiply()
    elif selection= 4:
         calculate_divide()
    else:
        print("sorry I dont undertsand your selection")

maincalculator()


def get_ticket_price():
    if age <= 7:
        return 8.00
    elif age <= 20:
        return 12.00
    elif age <= 60
        return 20.00
    else:
        return 0.00