#Files are used for storage because they last beyond the execution of the program.

# Opening a file in Python and reading it followed by printing its content
hosts = open('sample.txt')

# tell() : Determine the current position in the file.
print('Current position in the file is {}'.format(hosts.tell()))
host_file_content = hosts.read()
print('Contents of the file are {}'.format(host_file_content))
print('Current position in the file is {}'.format(hosts.tell()))

hosts.seek(0)
print('New position in the file is {}'.format(hosts.tell()))

hosts.seek(5)
print('New position in the file is {}'.format(hosts.tell()))

hosts.close()

print("Check if the file is closed or not")

if hosts.closed:
    print('File is closed')
else:
    print('File is not closed')

# Python has the provision of automatically closing a file.

print('Start reading the file')
with open('04_List.py') as hosts:
    new_host_file_content = hosts.read()
    print('Contents of the next file are {}'.format(new_host_file_content))
    print('Current position in the next file is {}'.format(hosts.tell()))

print('Checking if the file is closed?? {}'.format(hosts.closed))

# Reading file line by line
with open('04_List.py') as next_host:
    new_host_file_content_line = next_host.readline()
    for line in new_host_file_content_line:
        print(line)

