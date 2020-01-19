"""this is how you give
multi line comments"""

# exponentiation
# 2 ** 4 means 2 raised to the power 4
print('example of exponentiation ' + str(2**4))

# modulo operator
moduloExample = 3%2
print('example of modulo operator :: ' + str(moduloExample))

quanity_string=30
total_sum = quanity_string+20
total_diff = quanity_string-20
total_pdt = quanity_string*20
total_div = quanity_string/20

print("Values are ::  "+str(total_sum) + "   "+str(total_diff) + "  "+str(total_pdt) + "  "+str(total_div))

# boolean variables and functions
print("check if 1 is less than 2  "+str(1<2))
print("check if 1 is equal to 2  "+str(1==2))

# logicaloperations

print("check if 1 is less than 2 AND equal to 2 "+ (str(1<2) and str(1==2)))
print("check if 1 is less than 2 OR equal to 2 "+ (str(1<2) and str(1==2)))

# conditionals
if 30 > 40:
    print('inside if condition')
elif 30<40:
    print("inside elif")
else:
    print("inside else condition")