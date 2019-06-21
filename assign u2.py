#defining the function new_lines
def new_line():
    print('.')
    
#here function three_lines
def three_lines():
    new_line()
    new_line()
    new_line()

#nine_lines function is defined here
def nine_lines():
    three_lines()
    three_lines()
    three_lines()
nine_lines()
print ('Nine lines execution completed here')


#as defined in asignment here is the clear_screen function defined below
#here all together 4 new_line function is  called because when I followed the instruction properly I was able to print 22 lines only, So, I added 3 extra new_lines 
def clear_screen():
    new_line() 
    new_line()
    new_line()
    three_lines()
    print ( '15 Lines are executed succefully') #here I added this print statement because, I think it will be easy to count dots,
    nine_lines()
    new_line() 

clear_screen()

print ('Hi! we have %s printing %d lines' %('completed', 25)) #here %s acts as a placeholder for completed and %d acts as a placeholder for 25.
#%s is a placeholder for generic string or object and in case of object, It will be converted to string
#%d is a placeholder for decimal integer
