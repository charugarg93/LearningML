#Dictionary is a data type that holds key values called items
# they are also known as Associative arrays, hash tables and hashes.

# creating a dictionary
contact = {'python': '11111', 'java': '2222', 'scala' : '3333'}
print('list of all contacts are {}' .format(contact))

contact_java = contact["java"]
print('Contact of Python is {}'.format(contact_java))

# assigning new key value pairs to the dictionary
contact['c++']='4444'
print('new dictionary will be ::{}'.format(contact))

# removing items from dictionary
del contact['scala']
print(' dictionary after deletion will be ::{}'.format(contact))

# values inside the dictionary can have different data types
contact['ruby']=['5555', '6666']
print('New dictionary will be ::{}'.format(contact))

# checking if a key exists in the dictionary
if 'java' in contact.keys():
    print('key exists')
    print(contact['java'])
else:
    print('key doesnt exist')

# looping through the keys in a dictionary
for singleContact in contact:
    print('the number for {0} is {1}'.format(singleContact, contact[singleContact]))
