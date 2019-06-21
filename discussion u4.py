#universal gravatational constant(G) value is made global because this value doesn't change
G = 6.673*10**-11 #this value is for the part 2 of the assignment
import math
print ('Call the Function ev(m,r) where m is a mass and r is radius of earth, Value of M cannot be Zero\n    This is a small program to find the escape velocity of any Planet.') #Informing user about the precondition
def ev (m,r): #here m is a mass of a planet, r is the radius of the planet
    
    esv = (2*G*m)/r
    if m==0:
        print ('Precondition violated, mass cannot be zero')
        assert m > 0 #this is a precondition which makes sure that the value of mass is always greater than o, if the value of r is given 0 the zeroDivision Error occurs,so we don't need a precondition for r
        
    else:
        
        print ('The actual value of 2Gm divided by r is :', esv)
        escapevelocity = math.sqrt(esv)
        assert escapevelocity == 11184.480402811645 #this is a postcondition which makes sure that the escape velocity of earth is calculated properly, this also makes sure that the mass of earth and radius are are also correct
        print ('The escape velocity of Planet :' , escapevelocity,'m/s')  #the unit of answer is m/s (meter per second )
        return escapevelocity
#ev(5.98*10**24,6.38*10**6)
    #remove the comment from function call to find the exact value of escape velocity

