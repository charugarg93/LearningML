print('Start of the program')

# both are the examples of strings in python
fruit = 'Apple'
fruit2 = "apple"

sentence = 'this is the way to escape the character\'s punctuation mark'
print(sentence)

# printing the individual array element of the string
print(fruit[3])

# length function
print(len(fruit))

# String functions in python
print("String will be now printed in lower case:::",fruit.lower())
print("String will be now printed in lower case:::"+fruit.upper()+"  also this is how you concatenate the strings :::"+ fruit2)
print ('Repeat word 5 times without loop')
print ('Hello ' * 5 )

print("I want to test for formatting {0} in python. It is a good {1} ".format("option", "feature")  )

number = 5
print("concatenation of string is not possible with numbers"+ str(number))
# taking input from the user
user_input = input("please type something and press enter")
print('you entered ::::'+ user_input)