def soma(lista):
    if lista==[]:
        return 0
    else:
        ult=lista.pop()
        return ult + soma(lista)

# Test cases
print(soma([1, 2, 3, 4, 5]))  # Output: 15
print(soma([10, 20, 30]))      # Output: 60
print(soma([5, 10, 15, 20]))   # Output: 50
print(soma([]))                 # Output: 0