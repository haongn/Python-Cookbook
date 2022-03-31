# inline function: hàm trong cùng một dòng, hay chỉ có một dòng, không xuống dòng khác.   
# suy ra hàm gọi hàm callback trong thân hàm của nó là higher-order functions. 
# => inline function là một hàm rất ngắn gọn, là shortcut của hàm def (gọn gàng hơn). 


# Simple functions that do nothing more than evaluate an expression can be replaced by
# a lambda expression.

add = lambda x, y: x + y   
result = add(2, 3)
print(result)

result = add('hello', 'world')
print(result)

# The use of lambda above is the same as having typed this: 
def add(x, y):    
    return x + y    

print(add(2, 3))


# Typically, lambda is used in the context of some other operation, such as sorting or a 
# data reduction (higher-order function): 
names = ['Nguyen Duy Hao', 'Le Thi Hong Hanh', 'Pham Cong Minh', 'Pham Thi Hong Anh']
result = sorted(names, key = lambda name: name.split()[-1].lower())  # alphabetical order by default
print(result)








