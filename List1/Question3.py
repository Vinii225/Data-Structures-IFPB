# Exercise: Country class with name, capital, dimension, and border countries list.

class Country:
    def __init__(self, name, capital, dimension, border_countries=[]):
        self.__name=name
        self.__capital=capital
        self.__dimension=dimension
        self.__border_countries=border_countries
        
    def getName(self):
        return self.__name
    
    def getCapital(self):
        return self.__capital
    
    def getDimension(self):
        return self.__dimension
    
    def getBorderCountries(self):
        return self.__border_countries
    
    def addBorderCountry(self, country):
        if country not in self.__border_countries:
            self.__border_countries.append(country)
            
    def __str__(self):
        return f"Country: {self.getName()}\nCapital: {self.getCapital()}\nDimension: {self.getDimension()}\nBorders: {self.getBorderCountries()}"
    
country1 = Country("Brazil", "Brasília", 8515767)
country1.addBorderCountry("Argentina")
country1.addBorderCountry("Paraguay")
country1.addBorderCountry("Uruguay")
country1.addBorderCountry("Venezuela")
country1.addBorderCountry("Colombia")
country1.addBorderCountry("Guyana")
country1.addBorderCountry("Suriname")

country2 = Country("Argentina", "Buenos Aires", 2780400)
country2.addBorderCountry("Brazil")
country2.addBorderCountry("Paraguay")
country2.addBorderCountry("Uruguay")
country2.addBorderCountry("Bolivia")
country2.addBorderCountry("Chile")

print(country1, "\n")
print(country2, "\n")