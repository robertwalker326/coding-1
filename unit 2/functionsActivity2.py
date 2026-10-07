# problems #1
# create a function that will take in 2 inputs and 
# compare them.

# your inputs should be numbers.

# the functions should compare if the first input is
# less than the second input

# if it is less than the second input it
# should print true. If it is not, it should print false.


def comparevalue():
    valA= int (input())
    valB= int (input())
    print(valA < valB)


# problem #2
# create a function that will compare if a student
# has made honor roll.

# the student should be able to inpput 2 pieces of data
# the first should be their grade and the second should
# be the number of days they have been absent.

# if the students grade is above a 90 and the number
# of absenses is less than 5, the program should print
# true, otherwise it should print false 



def  checkhonor_roll():
    Grade = int (input())
    absences = int (input())
    print( Grade > 90 and absences < 5 )