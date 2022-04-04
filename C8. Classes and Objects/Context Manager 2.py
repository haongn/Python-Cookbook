

# Create a class that helps in file resource management. 
# The FileManager class helps in opening a file, writing/reading contents and then closing it.

class FileManager(): 
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None 

    def __enter__(self): 
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback): 
        self.file.close()


# Loading a file: 
with FileManager('test.txt', 'w') as f: 
    f.write('Test') 

print(f.closed)     # check if the opened file is close or note 



# File management using context manager and with statement :

# On executing the with block, the following operations happen in sequence:

# A FileManager object is created with test.txt as the filename and w(write) as the mode 
# when __init__ method is executed.

# The __enter__ method opens the test.txt file in write mode(setup operation) and returns 
# the FileManager object to variable f.

# The text ‘Test’ is written into the file.

# The __exit__ method takes care of closing the file on exiting the with block(teardown operation).

# When print(f.closed) is run, the output is True as the FileManager has already taken care of 
# closing the file which otherwise needed to be explicitly done (làm như này thì mình sẽ không 
# phải đóng file thủ công bằng tay nữa).