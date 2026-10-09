# when we are building complex, we need a
# way to pass in data that is not always
# from the user.

# Functions arguements and parameters are ways to
# pass in data to a function from possibly
# another function.

# function parameters-this is placeholders data for
# a function. variables inside the curly brackets

# memory trick- parameters placeholder both
# start with the letter P

def check_Water_Depth(depth):
 print(depth)
 print(depth > 10) # true if depth is greater than 10 feet
 #return depth

 # function arguemnt- this is the real data that we pass into
 # the function call
 # memory trick- if you make a real world arguemnt with a person
 # you need to come with real facts (data)
 check_Water_Depth(23)

 # return- this keyword allows us to pass from inside 1 function
 # into another function

def username():
    name = input("pleasetype in user name:")
    return name
 
 def confirmLogin():
    name = username()
    print(name)

 # username()
  confirmLogin():