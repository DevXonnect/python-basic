#part 1 create a long string
wordlist  = ['mac', 'pro',  'cat', 'nischal',  'shahi', 'thakuri','pasta','dog','rat','usa', 'nepal', 'china','winword']
sent = " Create a string that is a long series of words separated by spaces. The string is your own creative choice."
ext = ['hello', 'darkness']
word = wordlist[:]
#turn string into a list of words using split
delimiter = ' '



def wordwork(work):
    #Delete three words from the list, but delete each one using a different kind of Python operation.
    wordlist.pop(3)  #this line removes nischal from the wordlist
    #this loop removes shahi from the list
    while (wordlist.count('shahi')):
           wordlist.remove('shahi')      
    del wordlist[2] #deleting the cat from worlist. after deleting value  we cannot access it anymore
       
    #Sort the list. 
    word.sort()  # sorting the wordlist
        
    #Add new words to the list (three or more) using three different kinds of Python operation. 
    wordlist.append('Zebra') #adding the word to list method 1
    wordlist.extend(ext)  #here adding ext  to the wordlist, each word is split and added to the list
    wordlist.insert(2,'Xander') #here insert takes two arugments, 1 is the position where we want to insert the word and TEST is the word to insert

    print('Printing a list from a string.')
    #Turn the string into a list of words using split.
    spl =sent.split()     
    #Turn the list of words back into a single string using join.   
    print (spl) #string is splitted above and printed here
    print('\nJoining the list again.')
    get = delimiter.join(spl)    #string is joined here
    print(get)
 
   
wordwork(wordlist)
print('\n')
print ('All words including three new added words.')
print (wordlist)
print('\n')
print ('Below is the sorted list')
print(word)


#part 2


#nested list

nestedlist = ['Hi', 'this',['is', 'nischal'], 'shahi', ['a', 'proud', 'Nepali']]
print('\nPrinting example of nested list.')

print (nestedlist)

#the * operator
print('\nPrinting example of * operator.')
print ([nestedlist] *2)


#the list slice
print('\nPrinting example of list slice.')
print (wordlist[1:5])

#The “+=” operator
print('\nPrinting example “+=” operator')
ext += wordlist
print(ext)

#A list filter
print('\nPrinting example List Filter. Here all initial are capitalized')
def all_word_filter(ext):
    res = []
    for s in ext:
        res.append(s.capitalize())
    return res
print(all_word_filter(ext))
#a simple way to filter a string. capitalize makes the first word of sentence uppecase in case user forgets. 
test = ('this is a test string because python refused to capitalize the wordlist')
filter_words = test.capitalize()
print(filter_words)

#A list operation that is legal but does the "wrong" thing, not what the programmer expects
progress = ['a','s','d','f']
success = ['g','h','j']
print ('Printing an example of operations that is legal but does wrong.')
progress.append(['Hello world']) #  this is legal but it makes mistakes while printing the result. it adds the [] bracket as well as the quotation mark ''.
print(progress)


