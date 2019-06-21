import timeit # for timing the python code operation time

# creating tuple example

example = ('hi', 'UoPeople', 'Last ',  'week' , 'before exam')
print ('This is a Tuple')
print(example)
print('\n')
#creating list

example_list = ['this' , 'is '  , 'an' , 'example' , 'of list']
print ('This is a list')
print(example_list)
print('\n')
#exaple of tuple of string and list
example_list_tuple = ('this' , 'is' , [100] , '%' , 'nested example of tuple and list')
print ('This is example of nested tuple')
print (example_list_tuple)


#dictionary

dict = {'Name is' : 'Nischal' , 'last Name is ' : 'Shahi'}
output = dict.items()   # trhis is an item method
print('\n')
print (output)
#example of zip function

print('\n') #printing a new line before zip funciton
screen_output = zip(example, example_list)
print('This is example of zip')
print (list(screen_output)) # printing the output of zip funciton


# example of enumerate function

object1 = enumerate(example)
print('\n')
print ('This is an example of enumerate')
print(list(object1))




print('\n')
print ('This is the output to show tuple are faster than list and dictionary')

print (timeit.timeit('x = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)', number=10000000))
print (timeit.timeit('x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]', number=10000000))

print('Here each code runs for millions of time \
and outputs the overal time it took in seconds \n Here we can observe that Tuple is faster than List ')
