animals = ['cat', 'dog', 'elephant', 'whale', 'tiger', 'bear']
sorted_animals = sorted(animals)
print('Animal list is {}' .format(animals))

print('Sorted list of animals is {}' .format(sorted_animals))

all_animals = animals + sorted_animals
print('All animals list is {}'.format(all_animals))

# Printing length of an array

length = len(all_animals)
print('length of all animals is {}'.format(length))

# Range function generates a list of number is the specified range (not including the range number istelf)
for number in range(5):
    print(number)

# Range can also be used to print numbers within a given range using start and stop parameters
for n in range(8, 10):
    print(n)

# Range method used with start, stop and step parameter to tell how much difference is needed between 2 numbers
for step in range(1, 22, 4):
    print(step)

# using range in list of animals
for index in range(0, len(animals)):
    print(animals[index])