import math #importing math to use math.sqrt to square root the final values
#universal gravatational constant(G) value is made global because this value doesn't change
G = 6.673*10**-11 #this value is for the part 2 of the assignment

def hypotenuse (x,y): #defining a function which takes 2 arguments 
    squared = x**2 + y**2 #squaring the value of x and y
    print ( 'Value after adding square of X and Y : ', squared)
    answer = math.sqrt(squared) #doing the square root of value obtained from squared
    print ('The answer is:',answer) #printing the answer 
    return answer
   
hypotenuse(3,4)
hypotenuse(10,20)
hypotenuse(300,40)



#part 2
#here is a function that does a useful computation. Here is a formula to find the escape velocity of Planet

def ev (m,r): #here m is a mass of a planet, r is the radius of the planet 
    esv = (2*G*m)/r
    print ('The actual value of 2Gm divided by r is :', esv)
    escapevelocity = math.sqrt(esv)
    print ('The escape velocity of Planet :' , escapevelocity,'m/s')  #the unit of answer is m/s (meter per second )
    return escapevelocity 
    
ev(5.98*10**24,6.38*10**6)  #here 5.98*10**24 is the mass of earth in Kg,  and 6.38*10**6 is the radius of earth in meter 
ev(7.35*10**22,1.74*10**6) #this is the mass and the radius of moon
ev(5.683*10**26,5.82*10**5) #this is the mass and the radius of saturn 
