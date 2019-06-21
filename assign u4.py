def is_divisible(x, y): #a predefined function from textbook
    if x % y == 0:  # if x mudolo y is equal to 0 the return value is True or else false
        return True
    else:     
        return False
    
def is_power(a,b):  #defining a function is_power,  this is a text book exercise
   
    if a==b: #base case a == b this is a base case 
        return True
    elif b==1:
        return False    #calling is_divisible function as a return value inside is_power function
    else:
        return is_divisible(a,b) and is_power(a/b,b)
#test conditions provided in assignment page
print("is_power(10, 2) returns: ", is_power(10, 2)) 
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))




