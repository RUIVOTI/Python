# Tabuada

numero = input("Digite um numero da tabuada: ")
inicio = int(input("Digite um numero inical : "))
fim = int(input("Digite um numero final: "))

i = inicio

for i in range(inicio, fim + i):
    print(str(numero), "*", str(i), "=", int(numero) * i)
