# Estrutura de Dados

Este repositório contém implementações e exercícios da disciplina de Estrutura de Dados, focando em conceitos fundamentais de programação e estruturas de dados em Python.

## 📚 Objetivos da Disciplina
- Compreender conceitos fundamentais de Programação Orientada a Objetos
- Implementar e manipular estruturas de dados básicas
- Desenvolver habilidades de resolução de problemas usando Python

## 📁 Organização do Repositório

```
ED/
├── Slide1/              
│   ├── Question1.py    # Classes básicas
│   ├── Question2.py    # Retângulo e área
│   ├── Question3.py    # Conta Corrente
│   └── Question4.py    # Composição de objetos
│
├── List1/              
│   ├── Question1.py    # Classe Data
│   ├── Question2.py    # Sistema de Notas
│   ├── Question3.py    # Países e Fronteiras
│   └── Question4.py    # Sistema Bancário
│
└── LinearLists/        
    ├── Stack_(Pilha)/  
    │   └── pilha_encadeada.py
    └── Queue_(Fila)/   
        └── fila_encadeada.py
```

## 💡 Estruturas Implementadas

### Pilha (Stack)
- Estrutura LIFO (Last In, First Out)
- Métodos principais:
  - `empilhar(item)`: Adiciona um elemento no topo
  - `desempilhar()`: Remove o elemento do topo
  - `topo()`: Retorna o elemento do topo
  - `estaVazia()`: Verifica se a pilha está vazia

### Fila (Queue)
- Estrutura FIFO (First In, First Out)
- Métodos principais:
  - `enfileirar(item)`: Adiciona um elemento no final
  - `desenfileirar()`: Remove o primeiro elemento
  - `primeiro()`: Retorna o primeiro elemento
  - `estaVazia()`: Verifica se a fila está vazia

## 🚀 Como Usar

### Exemplo de uso da Pilha:
```python
pilha = PilhaEncadeada()
pilha.empilhar(10)
pilha.empilhar(20)
print(pilha.topo())  # Saída: 20
pilha.desempilhar()
print(pilha.topo())  # Saída: 10
```

### Exemplo de uso da Fila:
```python
fila = FilaEncadeada()
fila.enfileirar("A")
fila.enfileirar("B")
print(fila.primeiro())  # Saída: A
fila.desenfileirar()
print(fila.primeiro())  # Saída: B
```

## 🔧 Requisitos
- Python 3.x
- Conhecimentos básicos de POO

## 📝 Notas
- Todas as implementações seguem princípios de encapsulamento
- Códigos comentados para melhor compreensão
- Exercícios organizados por complexidade crescente