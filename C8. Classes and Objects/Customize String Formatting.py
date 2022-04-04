# Ta có thể tự tạo ra định dạng kiểu mới theo ý muốn (type specifying) thay vì những 
# định dạng kiểu có sẵn như f, b, e, x, X, ....

# create a new type of string formatting: 
_formats = {      # dictionary 
    'ymd': '{d.year}-{d.month}-{d.day}', # d: a (date) instance
    'mdy': '{d.month}/{d.day}/{d.year}', # month, day, year: the instance's attributes
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date: 
    def __init__(self, year, month, day): 
        self.year = year
        self.month = month
        self.day = day 

    def __format__(self, code):
        if code == '':              # if nothing passed 
            code = 'ymd'            # default date time  
        fmt = _formats[code]        

        return fmt.format(d = self) # replace d by self, and display the instance's attributes: month, year, day


if __name__ == '__main__':
    d = Date(2012, 12, 21)
    print(format(d))                        # no argument passed 
    print(format(d, 'mdy'))                 # direct argument pass 
    print('The date is {:ymd}'.format(d))   # type specifying (recommended - look professional)
    print('The date is {:mdy}'.format(d))  
    


