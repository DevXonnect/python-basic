import math #importing math for complex calculation

def my_sqrt(a):  #function mysqrt which takes a is defined here
    
    x =a/2  # the value of x is defined here
    while True:
         y = (x+a/x)/2.0
         if y == x:
             return y
             break
         x = y
         

def test_sqrt(test):  #here test_sqrt function is defined which takes test as a parameter    
    #this is the heading of table
    
    table_a = "a=" #for printing a inevery line
    
    
    table_line_a = "|" #this prints | after every value
    
    table_my_sqrt = "my_sqrt(a)=" #for printing my_sqrt(a) in every line 
   
    table_math_sqrt = "math.sqrt(a)=" #for printing math.sqrt(a) in every line 
 
    table_diff = "diff ="  #for printing diff in every line
   

  #defining a while loop 
    while True:   
        for a in test: 
            for_a =(a) 
            for_my_sqrt = my_sqrt(a)
            for_mathsqrt = math.sqrt(a)
            diff = abs(my_sqrt(a)-math.sqrt(a))  #abs means absolute value 
            print (table_a, for_a, table_line_a,
               table_my_sqrt, for_my_sqrt,table_line_a,
               table_math_sqrt, for_mathsqrt,table_line_a,
               table_diff ,   diff)   #this is just a print function 
            if a == 25:
                return a  #if the value of a reaches 25 then the loop breaks
                break
        
test_sqrt(range(1,26))  #here range is set to print 25 values, 

