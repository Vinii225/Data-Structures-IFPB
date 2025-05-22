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

class PilhaEncadeada:
    def __init__(self):
        self.__topo = None

    def estaVazia(self):
        return self.__topo is None

    def empilhar(self, item):
        novo_no = No(item)
        novo_no.setProximo(self.__topo)
        self.__topo = novo_no

    def desempilhar(self):
        if self.estaVazia():
            return None
        removido = self.__topo
        self.__topo = self.__topo.getProximo()
        return removido.getDado()

    def topo(self):
        if self.estaVazia():
            return None
        return self.__topo.getDado()

    def __len__(self):
        contador = 0
        atual = self.__topo
        while atual is not None:
            contador += 1
            atual = atual.getProximo()
        return contador

    def __str__(self):
        resultado = []
        atual = self.__topo
        while atual is not None:
            resultado.append(str(atual.getDado()))
            atual = atual.getProximo()
        return "Pilha(topo -> base): " + " -> ".join(resultado)

pilha = PilhaEncadeada()
print("\nTeste da Pilha Encadeada: ")
print("Pilha vazia? ", pilha.estaVazia())

pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)
print("\nApós empilhar: ", pilha)

print("\nTopo da pilha: ", pilha.topo())
print("Tamanho da pilha: ", len(pilha))

print("\nDesempilhando elementos: ")
print("Elemento removido: ", pilha.desempilhar())
print("Elemento removido: ", pilha.desempilhar())
print(pilha)