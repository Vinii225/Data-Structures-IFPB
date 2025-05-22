# Exercise: CurrentAccount class with a Client object as an attribute, demonstrating composition.

class CurrentAccount:
    def __init__(self, agency, client, balance):
        self.__agency=agency
        self.__client=client
        self.__balance=balance
        

    def getAgency(self):
        return self.__agency
    
    def getClient(self):
        return self.__client
    
    def getBalance(self):
        return self.__balance

    def setAgency(self, agency):
        self.__agency=agency
        
    def setClient(self, client):
        self.__client=client
        
    def setBalance(self, balance):
        self.__balance=balance
    
    def __str__(self):
        return f"\nAccount data\nAgency: {self.getAgency()}\n{self.getClient()}\nBalance: {self.getBalance()}"


class Client:
    def __init__(self, cpf, name):
        self.__cpf=cpf
        self.__name=name
        
    def getCpf(self):
        return self.__cpf
    
    def getName(self):
        return self.__name
    
    def setCpf(self, cpf):
        self.__cpf=cpf
        
    def setName(self, name):
        self.__name=name
        
    def __str__(self):
        return f"Client {self.getName()}\nCPF: {self.getCpf()}"

client1 = Client("123.456.789-00", "Vinicius")
current_account1 = CurrentAccount("001", client1, 85.00)
print(current_account1)

current_account1.setAgency("100")
current_account1.getClient().setCpf("098-765-432-11")
current_account1.getClient().setName("Ares")
current_account1.setBalance(100)
print(current_account1)