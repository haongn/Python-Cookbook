# Prob: You’ve written a function, but would like to attach some additional information to the
# arguments so that others know more about how a function is supposed to be used.

# chú ý: đây không phải type check, chỉ là một dạng comment cho đối số mà thôi. 

def add(x: int, y: int) -> int:     # note: this is not type checks 
    return x + y    


print(help(add))


print(add(10.2, 20.562))     # vì không phải type check nên ta cộng hai số thực vẫn oke. 
