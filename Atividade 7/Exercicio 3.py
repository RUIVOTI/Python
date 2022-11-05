# Calcule o fatorial de um numero.

def fatorial(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return n * fatorial(n - 1)
n = int(input("Digete um numero: "))

print("Fatorial de",n)
for i in range(n):
    n = fatorial(i+1)
    print(i+1,"-",n)
