# Capturing variables in anonymous functions: 
# Trái ngược với Default Arguments, thì tham số biểu thức lambda sẽ nhận giá trị của nó tại 
# thời điểm thực thi hàm, chứ không phải tại thời điểm định nghĩa hàm.  
# Ta có thể nói là tham số của biểu thức lambda là free variable (giống tham số bth). 

x = 10 
a = lambda y: x + y     

x = 20 
b = lambda y: x + y  


if __name__ == '__main__':
    print(a(10))     # 30 
    print(b(10))     # 30 
    #  the value of x used in the lambda expression is a free variable that gets 
    # bound at runtime, not definition time.


# If you want an anonymous function to capture a value at the point of definition and
# keep it, include the value as a default value: 
x = 10 
a = lambda y, x = x: x + y     # x is fixed at function definition time 

x = 20 
b = lambda y, x = x: x + y     # x is fixed at function definition time 

print(a(10))    # 10 + 10 = 20
print(b(10))    # 20 + 10 = 30 












