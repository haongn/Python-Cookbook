# generator function la ham co su dung tu khoa "yield".
# Unlike a normal function, a generator only runs in response to iteration.
# Generator có thể dùng nhiều câu lệnh yield trong thân hàm. 
# Generator sẽ chỉ dừng lại khi chạy đến hết hàm. 

# Tuc: chi khi su dung generator trong vong lap for, hoac su dung cau lenh next cho generator 
#      thì khi đó hàm generator mới chạy. 

def countdown(n): 
    print("Starting to count from", n)
    while n > 0: 
        yield n 
        n -= 1 
    print('Done!')


if __name__ == '__main__':
    c = countdown(3)        # create a generator, notice no output appears   
    print(c)
    print(next(c))          # run the first yield and emit a value
    print(next(c))          # run the second yield and emit the second value 
    print(next(c))          # run the third yield 
    print(next(c))          # print 'Done!' to the screen and raise StopIteration automatically 




