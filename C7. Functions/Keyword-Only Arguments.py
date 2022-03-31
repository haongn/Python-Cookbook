# we want to write a function that only accept certain arguments by keyword: 
# sol: This feature is easy to implement if you place the keyword arguments after a * argument
# or a single unnamed *.

# TH1: 
def recv(maxsize, *, block):  # block is the keyword-only argument 
    'Receives a message.'
    pass   
    

recv(1024, block = True)     # OK
# recv(1024, True)           # TypeError

# TH2: 
def recv(maxsize, *args, block): 
    'Receive a message.'
    pass      

recv(1024, block = True)     # OK 
# recv(1024, True)           # TypeError


print(help(recv))




