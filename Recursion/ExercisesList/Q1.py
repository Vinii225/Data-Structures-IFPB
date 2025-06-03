def potencia(x, n):
    if n==0:
        x=1
        return x
    elif n<0:
        return None
    else:
        return x * potencia(x, n-1) 

# Test cases
print(potencia(2, 3))  # Output: 8
print(potencia(5, 0))  # Output: 1
print(potencia(3, -2)) # Output: None
print(potencia(7, 2))  # Output: 49
print(potencia(10, 1)) # Output: 10 