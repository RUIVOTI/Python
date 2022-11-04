# • Faça um programa para imprimir

n = int(input("Digite para imprimir: "))

for i in range(n):
    for j in range(i+1):
        print(i+1, end="")
    print("")