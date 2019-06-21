prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
     print(letter + suffix)
     
print ("The output of Modified version of Progam is below")

 
prefixes = "JKLMNOPQ" #prefixes 
suffix = 'ack'
correction = 'uack' #this is to correct Oack and Qack 

for letter in prefixes:
    if letter == 'O' or letter == 'Q':  #checking words having initial O or Q if the word starts with O or Q then this statement will run and correct the word
        print(letter + correction)   #printing the corrected word
    else:
        print(letter + suffix)


#part 2
#"Give at least three examples that show different features of string slices."
#"Describe the feature illustrated by each example."
        

invent = "Give at least three examples that show different features of string slices. Describe the feature illustrated by each example."


print (invent[20]) #when we refer to a particular index number of string, python returns the character in that position, here in the string invent 20th character is e.

print(invent[76:]) #if we want to include the either end of a string, we can do that by not providing the value to either side the index number [a:b].
                   #In this example I am printing the back end of the string. Here the value of b is not provided to include all the sentences after 76th character.
 
print (invent[-8:-1])  #if we have a long string we can also count backward from the end of the string at the index number -1 to make our work easier.

print (invent[4:7]) #if we want to print the certain part of the string we can slice by creating a range of index numbers separated by a colon [a:b].

print (invent[:75:3]) #we can skip the characters after the first character we can do that by adding a second colon after the ending index number. [a:b:s] here
                      #here s is the skipping value after first character.  Here every third character are printed. Note: even whitespace are counted. 

