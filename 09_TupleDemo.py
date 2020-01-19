#tuple is an immutable list (i.e once defined cannot be changed) which is ordered and values are accessible via index

# Operations like concetenation, looping, iteration, negative indices and slicing are common in tuple just like in Lists

days_of_week = ('Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun')
monday = days_of_week[0]
print(monday)
# to print a blank line, we added one more print as follows
print()

for day in days_of_week:
    print(day)

# Modification of value is not possible for a tuple ;
try:
    days_of_week[2]='monday'
    print(days_of_week[2])
except:
    print('elements of a tuple cannot be modified')

# Deletion of the entire tuple is possible
del days_of_week
try:
    print("days of week are {}".format(days_of_week))
except:
    print('Tuple no longer exists')

# Switching between tuple and list
weekend_tuple = ('Sat', 'Sun')
list_weekend = list(weekend_tuple)
print('The type of weekend_tuple is {}'.format(type(weekend_tuple)))
print('The type of list_weekend is {}'.format(type(list_weekend)))
tuple_back_from_list = tuple(list_weekend)
print('The type of tuple_back_from_list is {}'.format(type(tuple_back_from_list)))

# looping through a tuple
for weekend in weekend_tuple:
    print(weekend)