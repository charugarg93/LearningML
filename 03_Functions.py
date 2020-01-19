def demoFunction():
    print('say hello')

def parametrizedFunction(parameter):
    print('the paramter passed is {}'.format(parameter))

# calling the function
demoFunction()
parametrizedFunction('demo')

def oddOrEvenFunction(number):
    if(number%2==0):
        print("number is even")
    else:
        print("number is odd")

oddOrEvenFunction(19)

def getName():
    name = input("What is your name")
    return name

def sayName(name):
    print('your name is {}.'.format(name))

def getAndSayName():
    """Def and"""
    name=getName()
    sayName(name)

getAndSayName()
