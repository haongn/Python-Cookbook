items = [1, 2, 3]

# get the iterator: 
it = iter(items)      # invokes items.__iter__()

# run the iterator: 
print(next(it))       # invokes it.__next__()
print(next(it))
print(next(it))
# print(next(it))       # raise StopIteration error 

# ta cung co the su dung vong lap for cho iterator: 
it = iter(items)
print(type(it))
for ele in it: 
    print(ele)

    