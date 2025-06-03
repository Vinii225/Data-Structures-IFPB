def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Test cases
print(fibonacci(1))  # Output: 0
print(fibonacci(2))  # Output: 1
print(fibonacci(3))  # Output: 1
print(fibonacci(4))  # Output: 1
print(fibonacci(5))  # Output: 2
print(fibonacci(6))  # Output: 3
print(fibonacci(7))  # Output: 5