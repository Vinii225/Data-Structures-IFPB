# Considere que todas as estruturas devem ser implementadas de forma encadeada
# 1. Implemente o método para inserir um elemento na fila.
# 2. Implemente o método para remover um elemento na fila.
# TODO: 3. Implemente o método para concatenar para a fila.
# 4. Implemente o método para imprimir os elementos da fila.
# 5. Implemente o método para inserir um elemento na pilha.
# 6. Implemente o método para remover um elemento na pilha.
# 7. Implemente o método para obter um elemento da posição X da pilha.
# TODO: 8. Implemente o método para inverter a pilha.
# 9. Implemente o método para inserir um elemento na lista.
# 10. Implemente o método para remover um elemento na lista.
# TODO: 11. Implemente o método para checar_duplicidade da lista.
# 12. Implemente o método para obter um elemento da posição X da lista.
# 13. Implemente o método para alterar o valor de uma posição X da lista.


# Question 1
def inserir_fila(self, dado):
    novo = No(dado)
    if self.vazia()==True:
        self.inicio = novo

    else:
        p = self.inicio
        while p.prox is not None:
            p = p.prox
        p.prox = novo

# Question 2 
def remover_fila(self):
    if self.vazia():
        return None
    
    removido = self.inicio.dado
    self.inicio = self.inicio.prox
    return removido

# Question 4
def imprimir_fila(self):
    fila_list=[]
    if self.vazia()==True:
        return "Vazia"
    
    else:
        p = self.inicio
        while p.dado is not None:
            fila_list.append(p.dado)
            p = p.prox
        return fila_list
    
# Question 5
def inserir_pilha(self, dado):
    novo = No(dado)
    if self.vazia()==True:
        self.topo = novo

    else:
        novo.prox=self.topo
        self.topo=novo
    return "Inserido"

# Question 6
def remover_pilha(self):
    if self.vazia():
        return None
    
    else:
        removido=self.topo
        self.topo=self.topo.prox
    return removido

# Question 7
def elemento_posicao(self, posicao):
    if self.vazia() or posicao < 1:
        return None
    
    count=1
    aux=self.topo
    while aux is not None:
        if count==posicao:
            return aux.dado
        
        aux=aux.prox
        count+=1

# Question 9
def inserir_lista(self, dado, posicao):
    novo=No(dado)
    if self.vazia():
        self.inicio=novo
        return "Inserido"
    
    else:
        if posicao==0:
            novo.prox=self.inicio
            self.inicio=novo
            return "Inserido"
    
        if posicao>=self.tamanho():
            aux=self.inicio
            while aux.prox!=None:
                aux=aux.prox
            aux.prox=novo
            return "Inserido"


        else:
            p=self.inicio
            q=None
            count=1
            while count<posicao:
                q=p
                p=p.prox
                count+=1

            novo.prox=p
            q.prox=novo
            return "Inserido"
        
# Question 10