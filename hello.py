import random
import sys
import os

print ('Hello Bhosoos!')

#comment(single line)

'''
Multi line
comment
'''

name="Shubham"
print(name)

# Numbers, strings, lists, tuples, dictionaries

print(5//2)
print(5**2)

var=90;

print("Value of var is:",var)

#lists

grocery_list=['Juice', 'Tomatoes', 'Potatoes']
print('First Item', grocery_list[0])
print(grocery_list)

print(grocery_list[1:3])
grocery_list.insert(2,'Rohoot')
print(grocery_list)

grocery_list.sort()
print(grocery_list)

grocery_list.reverse()
print(grocery_list)

del grocery_list[2]
print(grocery_list)

def add2Number(n1,n2):
    return n1+n2

sum=add2Number(2,5)
print(sum)
'''
print("Enter an integer.")
int=sys.stdin.readline()
print('Entered integer is:',int)
'''

string="blacked"
print(string[1:])


