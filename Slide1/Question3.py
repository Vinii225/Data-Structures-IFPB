# Exercise: CurrentAccount class with agency, cpf, name, and balance, including setters and getters.

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

    def setAgency(self, agency):
        self.__agency=agency
    
    def setCpf(self, cpf):
        self.__cpf=cpf
    
    def setName(self, name):
        self.__name=name
    
    def setBalance(self, balance):
        self.__balance=balance
    
    def __str__(self):
        return f"\nAccount data\nAgency: {self.getAgency()}\nCPF: {self.getCpf()}\nName: {self.getName()}\nBalance: {self.getBalance()}"
    
current_account1 = CurrentAccount("001", "123.456.789-00", "Vinicius", 85.00)
print(current_account1)

current_account1.setAgency("100")
current_account1.setCpf("098-765-432-11")
current_account1.setName("Ares")
current_account1.setBalance(100)
print(current_account1)