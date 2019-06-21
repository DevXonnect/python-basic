#a function that takes an arugments and parameters is defined below
from math import pi
#here (x,y) are the parameters
def funx(x,y):
    print (x+y)
# values (1,2) are the arguments.
funx(1,2)
#calling a function using a variable, this is a function call using a variable arguments
funx('CS','1101')
#calling a function using an expression, this is a simple function call using an math expression
funx(2*4**2,5/2 + pi/ (2))
#a test function call, this is just a test function call using variables and math operator 
funx('Test' , ' Test' * 2)


#Exmple 3,  Creating a function with a local variable

def funV():
    v = "This is a local variable"
    print(v)
    
funV()

#Try to print the 'v' outside of the function, and see what error we get. 

#Example 5, When a variable defined outside a function has the same name as a locl variable insidea function.

y = 'I am an error'
def same_name():
    y = 'I am trying to overwrite Y'
    print (y)
same_name()   #calling the function (same_name)
print (y)   # calling a variable described outside the function (same_name)


#Example 4,  Create a function that takes an argument.
#here moss and fern are the two different parameters and the 

def funxpara(param):
     print (param, 'Hey, Thanks for stopping by')
 
funxpara(0)
