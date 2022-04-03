class Date:
    def __init__(self, string:str):
        self.string = string
    
    @classmethod
    def integer(cls, string):
        year = int(string[string.rfind('.')+1:])
        month = int(string[string.find('.')+1:string.rfind('.')])
        day = int(string[:string.find('.')])
        
        return day, month, year
    
    @staticmethod
    def validate(day, month, year):
        if not year > 0:
            return f'The date {day}.{month}.{year} is not correct'
        
        if not  1 <= month <= 12:
            return f'The date {day}.{month}.{year} is not correct'
        
        if month == 2 and not 1<=day<=28:
            return f'The date {day}.{month}.{year} is not correct'
        
        elif month in [1, 3, 5, 7, 8, 10, 12] and not 1<=day<=31:
            return f'The date {day}.{month}.{year} is not correct'
        
        elif month in [2, 4, 6, 9, 11] and not 1<=day<=30:
            return f'The date {day}.{month}.{year} is not correct'
        
        

date1 = Date('11.10.2021')
day, month, year = Date.integer('31.04.2022')
print(day, month, year)
print(Date.validate(day, month, year))