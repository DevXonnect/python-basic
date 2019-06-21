def countdown(n):

     if n <= 0: #n is less than or equal to 0

          print('Blastoff! You entered a positive number')

     else:

          print(n)

          countdown(n-1)



#defining a countup function

def countup(n):

    if n >= 0: #n is greater of equal to 0

        print ('Blastoff! You entered a negative number')

    

    else:

        print (n) 

        countup (n+1)

#defining function for 0 input

def zerofunx(n):

    print ("You made a wrong choice")



#defining a function for taking keyboard inputs    

def userinp():

    n = int(input('Enter negative or positive numbers \n')) #here \n is for new line

    if n==0:  #if the user inputs 0 as a value function zerofunx will execute

        zerofunx(n)

    elif n<=0: #if the user inputs negative number function countup will execute

        countup(n)

 

    else: #if positive integer is given coundown will start

        countdown(n)

          

userinp()

