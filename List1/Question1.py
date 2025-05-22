# Exercise: Date class with day, month, and year attributes, including setters and string representation.

class Date:
    def __init__(self, day, month, year):
        self.__day=day
        self.__month=month
        self.__year=year
        
    def getDay(self):
        return self.__day
    
    def getMonth(self):
        return self.__month
    
    def getYear(self):
        return self.__year
    
    def setDay(self, day):
        self.__day=day
        
    def setMonth(self, month):
        self.__month=month
        
    def setYear(self, year):
        self.__year=year
    
    def __str__(self):
        return f"Date: {self.getDay()}/{self.getMonth()}/{self.getYear()}"
    
date1 = Date(5, 11, 2004)
print(date1)

date1.setDay(31)
date1.setMonth(12)
date1.setYear(2025)
print(date1)