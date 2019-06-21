d={ 'Radius of the Sun': '695,510 km', 'Radius of the Earth': '6,371 km', 'Radius of the Moon': '1,737.1 km' }


print("intial_dictionary", str(d)) #for printing the original dictionary
print ('\n')
#function from the textbook
def invert_dict(d):
     inverse = dict()
     for key in d:
          val = d[key]
          if val not in inverse:
               inverse[val] = [key]
          else:
               inverse[val].append(key)
     return inverse
print ('Inverted dictionry',(invert_dict(d)))  #printing the inverted dictionary
print ('\n')

#modified function to print the keys
def invert_dicts(d):
    return d.keys()
print (invert_dicts(d))


print ('\n')

def invert_dicti(d):
    ans = list(d.items())
    return ans
    
print ('Dictionary list',(invert_dicti(d)))

'''
#code below is a code to print keys and values
print ('\n')
print("intial_dictionary", str(d))
def invert_dictss(d):
    keys = []
    values =[]
    items = d.items()
    for item in items:
        keys.append(item[0]), values.append(item[1])
     
        print ("keys : ", (keys))
        print ('values : ', (values))
print (invert_dictss(d))  '''
       
        
 
