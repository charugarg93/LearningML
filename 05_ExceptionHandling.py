# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)

# Program to depict else clause with try-except

# Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

animals = ['cat', 'dog', 'elephant']
index_Animal = animals.index('dog')
print("Index of the element is :: {}.".format(index_Animal))
try:
    index_Animal = animals.index('whale')
except:
    index_Animal= "animal not found in the list"

print(index_Animal)
