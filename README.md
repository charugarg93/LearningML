The Python implementation compiles the files as needed. For this reason, Java is often called a compiled language, while Python is called an interpreted language. 

Basic Foundation course completed from Udemy : Cert No UC-4N5MURKW
***Folder contains the pdf of the certification of completion***
KEY POINTS

1. To launch the python IDE, type idle3 on the terminal.
2. In python, Asterisk (*) is the repetition operator, ie,   
print ('-' * 5 ) will give -----
3. multi line comments can be given by triple quotes.
4. -1 index returns the last element of the list, -2 returns second last item of the list and so on.
5. Range function can be used to print range of numbers starting from 0 to range specified (not including the range number istelf) or to print numbers within a given range using ***start and stop parameters***; Range method is also used with ***start, stop and step parameter*** to tell how much difference is needed between 2 numbers.
6. Tuple is an immutable list (i.e once defined cannot be changed) which is ordered and values are accessible via index. They are used when you dont wish the data to be changed. We can switch between tuple and list by writing : ***list_from_tuple = list(tuple_name)*** and ***tuple_from_list=tuple(list_name)***
7. While reading a p=file, python keeps track of your current position in the file:

    a. read() : method returns the entire file.
    b. seek(offset) : change the current position to offset.
    c. seek(0) : Go to the beginning of the file.
    d. seek(5) : Go to the 5th byte of the file.
    e. tell() : Determine the current position in the file.
    f. close() : close the file once the operation has been performed.
8. Python has the provision of automatically closing a file by writing ***with open('file_path') as variable_name***
9. We can specify the mode as well while opening a file ***open('file_path', mode)*** The different modes are:
    a. r : read ((default))
    b. w : write
    c. x : create a new file and oepn it for writing
    d. a : open for writing, appending to a file
    e. + : open a file for updating (read/write)
    f. b : binary files
    g. t : text mode (default)
We can give mulitple modes aslo like : rb, w+ and so on.
10. A module can be implemented in another Python program using import statement followed by the module name.    

**Here is the list of topics covered in each program**:

1. basicSyntax has the syntax about variables, strings, string operations like lower, upper, concatenation, repetition operator *, and finally how to take input from the user and print it.
2. Operations has syntax on arithmetic operators, booleans, logical operators, conditionals(if-else, elif)
3. Function has syntax for non parametrized functions, parametrized functions, recursive functions.
4. List has syntax for creating and accessing the list, using negative indices, append method to append items at the end of the list, extend method to add multiple items in a list, slicing to access elements between 2 indices, deleting elements of list
5. ExceptionHandling has syntax for writing try block and handle exception
6. LoopDemo has syntax for writing for loop, while loop
7. SortingAndRanges has the syntax for sorting a list, how to print the length of an array, using range function to print the range of numbers starting from 0 to range specified (not including the range number istelf); Range can also be used to print numbers within a given range using start and stop parameters; Range method is also used with start, stop and step parameter to tell how much difference is needed between 2 numbers; using range for a list of strings.
8. DictionariesDemo has the info on Dictionary, how are they created, how new key value pairs are added/ deleted from an existing dictionary, checking if a key exists in a dictionary, looping through a dictionary.
9. TupleDemo has the details on Tuple (which is an immutable list), how values within tuple cannot be modified, only the tuple can be completely deleted, showing how to switch between tuple and list.
10. FilesDemo has syntax for opening a file, reading the content of it and then printing it, using tell method to tell the current location, seek method to go to a specified offset, closing a file manually, automatically closing a file, reading the file line by line, modes of opening a file.
11. ModulesDemo has the syntax for importing other modules, importing just the method or just a given attribute of another module
11. ModulesDemo has the syntax for importing other modules, importing just the method or just a given attribute of another module


