
books = ['kanetkar', 'ritchie', 'tanenbaum']
print(books[2])

# in python you can also have negative indices
# -1 denotes last element of the list, -2 denotes second last item of the list and so on

print("Experimenting with negative indices ::: "+ books[-3])
books.append("galvin")
print(books)

#  extend method is used to add multiple items in a list
books.extend(['rosen','headfirst', 'cormen'])
print(books)

more_books = ['kreyzig', 'mitchel']
books.extend(more_books)

# print("Newly added books::: "+more_books)
print(books)

# slices are used to access the elements from one index to another
# this will print elements from index 1 to 3. 4 will be excluded
print(books[1:4])

my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])
# elements beginning to 4th
print(my_list[:-5])
# elements 6th to end
print(my_list[5:])
# elements beginning to end
print(my_list[:])

# deleting elements of list
my_list = ['p','r','o','b','l','e','m']
# delete one item
del my_list[2]
# Output: ['p', 'r', 'b', 'l', 'e', 'm']
print(my_list)
# delete multiple items
del my_list[1:5]
# Output: ['p', 'm']
print(my_list)
# delete entire list
del my_list
# Error: List not defined
print(my_list)