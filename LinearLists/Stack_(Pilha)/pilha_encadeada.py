class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        self.__topo = None

    def Vazia(self):
        return self.__topo is None

    def empilhar(self, item):
        novo_no = No(item)
        novo_no.proximo = self.__topo
        self.__topo = novo_no

    def desempilhar(self):
        if self.Vazia():
            return None
        removido = self.__topo
        self.__topo = self.__topo.proximo
        return removido.dado

    def __str__(self):
        dados = ''
        p = self.__topo
        while(p != None):
            dados = dados + ' ' + str(p.dado)
            p = p.proximo
        return dados


pilha = PilhaEncadeada()
print(f"Pilha vazia? {pilha.Vazia()}")

pilha.empilhar("A")
pilha.empilhar("B")
pilha.empilhar("C")
print(pilha)

print(f"Removido: {pilha.desempilhar()}")
print(f"Removido: {pilha.desempilhar()}")
print(pilha)