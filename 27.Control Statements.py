# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6, 2019

File: Loops and Control Statement (continue, break and pass)
@author: Byen23
"""
from __future__ import print_function 

print("---" * 20)	

print("\nPrints Hello world 3 times, where while loop is used for iterators.\n")
count = 0 
while (count < 3):
	count = count+1
	print("Hello World")
	
print("---" * 20)	

# For in Loop, iterating over a list
print("List Iteration\n")

l = ["Hello", "World", "!"]
for i in l:
	print(i)

print("---" * 20)
	
# Iterating over a tuple(immutable)
print("Tuple Iteration\n")
t = ("Hello", "World", "!")
for i in t:
	print(i)

print("---" * 20)
	
# Iterating over a String
print("String Iteration\n")
s = "Hello"
for i in s:
	print(i)

print("---" * 20)
	
# Iterating over a dictionary
print("Dictionary Iteration\n")
d = dict()
d["xyz"] = 123
d["abc"] = 345
for i in d:
	print("%s %d" %(i, d[i]))

print("---" * 20)

# Nested Loops
"""
We can put any type of loop insie of any other type of loop. For example, a for loop can be inside a while loop or vice versa.
"""
print("Nested Loops\n")
for i in range(1, 5):
	for j in range(i):
		print(i, end=' ')
	print()
	
print("---" * 20)

# Loop Control Statements
"""
Loop control statements change execution from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed.
"""

# Continue Statement
"""
It returns the control to the beginning of the loop.
"""
print("Continue Statements\n")
# Prints all letters except 'e' and 's'
for letter in ("HelloWorld!"):
	if letter == ('e') or letter == ('s'):
		continue
	print("Current Latter : ", letter)
	var = 10
	
print("---" * 20)	

# Break Statement
"""
It brings control out of the loop.
"""
print("Break Statement\n")
for letter in ("HelloWorld!"):
	# break the loop as soon as it sees 'e'
	# or 's'
	if letter == ('e') or letter == ('s'):
		break
print("Current letter :", letter)

print("---" * 20)	

# Pass Statements
"""
We use pass statement to write empty loops. Pass is also used for empty control statement, function and classes.
"""

print("Pass Statement\n")

# An empty loop
for letter in ("HelloWorld"):
	pass
print("Last Letter :", letter)




