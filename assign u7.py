alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"] 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"] 

# From Section 11.2 of: 

# Downey, A. (2015). Think Python: How to think like a computer scientist. Needham, Massachusetts: Green Tree Press. 

def histogram(s):
     d = dict()
     for c in s:
          if c not in d:
               d[c] = 1
          else:
               d[c] += 1
     return d

#part 1
def has_duplicates(s):  #defining the has_duplicate function
     h = histogram(s)
     duplicates = [key for key, value in h.items() if value > 1] 
     return duplicates if duplicates else None   #here duplicates is retured to show the user which are the duplicate characters
 #part for printing the result
for letters in test_dups:    
     if has_duplicates(letters) == None:
          print (letters, 'has no duplicates')
     else:
          print (letters, 'has duplicates', has_duplicates(letters))



print ('\n')
print ('Part 2 of the assignent')
print('\n')
#part 2 of the assignme 
def missing_letters(d):  #defining the missing_letters function
    compare = histogram(d) 
    for key in sorted(compare): 
        if key in alphabet: 
            answer = alphabet.replace(key,'')   #here answer is stored in answer 
            return answer #returning the result from answer 
        else:
            return None
 #part for printing the result
for letters in test_miss: 
    if missing_letters(letters) == None:
        print(letters, 'uses all the letters')   
    else:
        print(letters , 'is missing letters', missing_letters(letters))
     
