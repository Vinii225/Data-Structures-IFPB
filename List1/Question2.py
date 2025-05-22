# Exercise: Student class with id, name, and grades list, including average calculation.

class Student:
    def __init__(self, id, name, grades=[]):
        self.__id=id
        self.__name=name
        self.__grades=grades
        
    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def setId(self, id):
        self.__id=id
        
    def addGrade(self, grade):
        self.__grades.append(grade)
        
    def getMedia(self):
        manual_sum=0
        for grade in self.__grades:
            manual_sum+=grade
        return manual_sum/len(self.__grades)
            
    def setName(self, name):
        self.__name=name
        
    def __str__(self):
        return f"ID: {self.getId()}\nName: {self.getName()}\nAverage: {self.getMedia():.2f}"
    
student1 = Student("20242370007", "Vinicius")
student1.addGrade(8)
student1.addGrade(9)
student1.addGrade(10)
print("\n", student1, "\n")