# We create a simple database connection management system. 
# The number of database connections that can be opened at a time is also limited 
# (just like file descriptors). 
# Therefore context managers are helpful in managing connections to the database as there 
# could be chances that the programmer may forget to close the connection.

from pymongo import MongoClient


class MongoDBConnectionManager(): 
    """Create a simple database connection management system.

    The number of database connections that can be opened at a time is limited.

    Therefore context managers are helpful in managing connections to the database as there 
    could be chances that the programmer may forget to close the connection."""

    class MongoDBConnectionManager(): 
        def __init__(self, hostname, port): 
            self.hostname = hostname
            self.port = port
            self.connection = None     # there is no connection at setup stage

        def __enter__(self):    
            self.connection = MongoClient(self.hostname, self.port)
            return self 

        def __exit__(self, exc_type, exc_value, exc_traceback): 
            self.connection.close()    # automatically close the connection 


# Connecting with a localhost: 
with MongoDBConnectionManager('localhost', '27017') as mongo: 
    collection = mongo.connection.SampleDb.test   
    data = collection.find({'_id': 1})
    print(data.get('name'))


# Database connection management using context manager and with statement :

# On executing the with block, the following operations happen in sequence:

# A MongoDBConnectionManager object is created with localhost as the hostnamename and 27017 as 
# the port when __init__ method is executed.

# The __enter__ method opens the mongodb connection and returns the MongoDBConnectionManager 
# object to variable mongo.

# The test collection in SampleDb database is accessed and the document with _id=1 is retrieved. 
# The name field of the document is printed.

# The __exit__ method takes care of closing the connection on exiting the with block 
# (teardown operation).


