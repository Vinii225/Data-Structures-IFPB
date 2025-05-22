# Exercise 1: Rectangle class with height and base attributes, and string representation.
class Rectangle:
    def __init__(self, height, base):
        self.__height=height
        self.__base=base

    def getHeight(self):
        return self.__height
    
    def getBase(self):
        return self.__base
    
    def __str__(self):
        return f"\nRectangle attributes\nHeight: {self.getHeight()}\nBase: {self.getBase()} "

rectangle1 = Rectangle(5, 4)
print(rectangle1)


# Exercise 2: Student class with name, id, and course attributes, and string representation.
class Student:
    def __init__(self, name, id, course):
        self.__name=name
        self.__id=id
        self.__course=course

    def getName(self):
        return self.__name
    
    def getId(self):
        return self.__id
    
    def getCourse(self):
        return self.__course
    
    def __str__(self):
        return f"\nStudent data\nName: {self.getName()}\nID: {self.getId()}\nCourse: {self.getCourse()}"

student1 = Student("Vinicius", "20242370007", "Sistemas para Internet")
print(student1)  


# Exercise 3: CurrentAccount class with agency, cpf, name, and balance attributes, and string representation.
class CurrentAccount:
    def __init__(self, agency, cpf, name, balance):
        self.__agency=agency
        self.__cpf=cpf
        self.__name=name
        self.__balance=balance

    def getAgency(self):
        return self.__agency
    
    def getCpf(self):
        return self.__cpf
    
    def getName(self):
        return self.__name
    
    def getBalance(self):
        return self.__balance
    
    def __str__(self):
        return f"\nAccount data\nAgency: {self.getAgency()}\nCPF: {self.getCpf()}\nName: {self.getName()}\nBalance: {current_account1.getBalance()}"
    
current_account1 = CurrentAccount("001", "123.456.789-00", "Vinicius", 85.00)
print(current_account1)