#example for simple chained conditional
#here x and y are the global variables which I will be using for both nested and chained conditional examples
x = 20
y = 30

if x > y:
    print ('X is greater than Y')
elif x < y:
    print ('X is smaller than Y')
elif x==y:
    print ('X is equal to Y')
else:
    print ('X and Y might be Equal')
    
#here is another simple chained conditional where x is smaller than y
def chainfunx(x,y):
    if x > y :
        print ('X is greater than Y')
    elif x < y:
        print ('X is smaller than Y')
    elif x==y:
        print ('X is equal to Y')
chainfunx(10,20)


#example for simple nested conditional
if x < y:
    print ('X is less than Y')
else:  #here if and else are the nested conditionals of else branch 
    if x > y:
        print ('X is greater than Y')
    else:
        print('X and Y is equal')

def nestedfunx(x,y):
    if x > y:
        print ('X is greater than Y')
    else: #here if and else are the nested conditionals of else branch 
        if x < y:
            print('X is less than Y')
        else:
            print ('X must be equal to Y')
nestedfunx(10,0)


#defining function to take input from user to check conditions
def userinput():
    #here input().split() is a syntax to take 2 input from user
    x,y = input('Enter value for X and Y. This is an example of chained conditional.\nPlease look the code to see the example of chained conditional.\nPlease leave a space between numbers.\n').split() #here \n is a code for displaying new line 
    if x > y:
        print ('X is greater than Y')
    elif x<y:
        print('X is smaller than Y')
    elif x==y:
        print('X is equal to Y')

userinput()

#defining a function to take input from user for nested conditionals
def nuserinput():
    #here input().split() is a syntax to take 2 input from user
    x,y = input('Enter value for X and Y. This is an example of nested conditional.\nPlease look the code to see the example of nested conditional.\nPlease leave a space between numbers.\n').split() #here \n is a code for displaying new line 
    if x > y:
        print ('X is greater than Y')
    else: #here if and else are the nested conditionals of else branch 
        if x < y:
            print('X is less than Y')
        else:
            print ('X must be equal to Y')

nuserinput()


