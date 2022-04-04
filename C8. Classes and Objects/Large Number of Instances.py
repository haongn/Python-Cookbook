# You should only use slots on classes that are going to serve as frequently used data structures 
# in your program (e.g., if your program created millions of instances of a particular class)

# Classes that define slots don’t support certain features such as multiple inheritance.

# Ví dụ như Node như trong Tree, Linked List vậy, vì nó phục vụ như là một cấu trúc dữ liệu, 
# và không có inheritance.


class Date: 
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day): 
        self.year = year 
        self.month = month
        self.day = day




    