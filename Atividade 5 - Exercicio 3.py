# Crie um programa com uma função para multiplicar dois números e o algoritmo mostrar o resultado.

def multiplicar(n1, n2):
    resultado = n1 * n2
    return resultado

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

print("O resultado",n1, "*", n2, "=", multiplicar(n1, n2))
