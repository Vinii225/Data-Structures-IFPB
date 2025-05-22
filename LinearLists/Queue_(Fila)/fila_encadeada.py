class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class FilaEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def Vazia(self):
        return self.__inicio is None

    def enfileirar(self, item):
        novo_no = No(item)
        if self.Vazia():
            self.__inicio = novo_no
            self.__fim = novo_no
        else:
            self.__fim.proximo = novo_no
            self.__fim = novo_no

    def desenfileirar(self):
        if self.Vazia():
            return None
        removido = self.__inicio
        self.__inicio = self.__inicio.proximo
        if self.__inicio == None:
            self.__fim = None
        return removido.dado

    def __str__(self):
        dados = ''
        p = self.__inicio
        while(p != None):
            dados = dados + ' ' + str(p.dado)
            p = p.proximo
        return dados


fila = FilaEncadeada()
print(f"Fila vazia? {fila.Vazia()}")


fila.enfileirar("A")
fila.enfileirar("B")
fila.enfileirar("C")
print(fila)


print(f"Removido: {fila.desenfileirar()}")
print(f"Removido: {fila.desenfileirar()}")
print(fila)