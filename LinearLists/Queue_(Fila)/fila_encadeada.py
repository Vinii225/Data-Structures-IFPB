class No:
    def __init__(self, dado, proximo=None):
        self.__dado = dado
        self.__proximo = proximo

    def getDado(self):
        return self.__dado

    def setDado(self, dado):
        self.__dado = dado

    def getProximo(self):
        return self.__proximo

    def setProximo(self, proximo):
        self.__proximo = proximo

    def __str__(self):
        return f"{self.__dado}"

class FilaEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def estaVazia(self):
        return self.__inicio is None

    def enfileirar(self, item):
        novo_no = No(item)
        if self.estaVazia():
            self.__inicio = novo_no
            self.__fim = novo_no
        else:
            self.__fim.setProximo(novo_no)
            self.__fim = novo_no

    def desenfileirar(self):
        if self.estaVazia():
            return None
        removido = self.__inicio
        self.__inicio = self.__inicio.getProximo()
        if self.__inicio is None:
            self.__fim = None
        return removido.getDado()

    def primeiro(self):
        if self.estaVazia():
            return None
        return self.__inicio.getDado()

    def __len__(self):
        contador = 0
        atual = self.__inicio
        while atual is not None:
            contador += 1
            atual = atual.getProximo()
        return contador

    def __str__(self):
        resultado = []
        atual = self.__inicio
        while atual is not None:
            resultado.append(str(atual.getDado()))
            atual = atual.getProximo()
        return "Fila(início -> fim): " + " -> ".join(resultado)