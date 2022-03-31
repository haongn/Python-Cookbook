# Function overloading is the ability to have multiple functions with the same name but with 
# different signatures/implementations. 

# When an overloaded function fn is called, the runtime first evaluates the arguments/parameters 
# passed to the function call and judging by this invokes the corresponding implementation.

# Hiểu đơn giản là khi truyền tham số vào thì sẽ xét số lượng và kiểu của đối số 
# để có thể sử dụng được hàm thích hợp mong muôn.

# Python does not support function overloading. When we define multiple functions with the same 
# name, the later one always overrides the prior and thus, in the namespace, there will always 
# be a single entry against each function name.

# We see what exists in Python namespaces by invoking functions locals() and globals(), which 
# returns local and global namespace respectively.


def area(radius): 
    return 3.14 * radius * 2

def product(a, b): 
    return a * b 

def product(a, b, c): return a * b * c


if __name__ == '__main__':
    print(product(2, 3, 4))
    # print(product(2, 3))     # raise TypeError


print(locals())     # return local namspace




