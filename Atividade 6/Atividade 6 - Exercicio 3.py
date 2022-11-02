# Casal De Coelhos

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 12

print("“Ao final de um ano" ,fibonacci(n), "casais de coelhos estaram no patio")