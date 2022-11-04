# Faça um Programa que leia em um vetor de 10 caracteres (letras ) e diga quantas consoantes foram lidas.
# Mostre as consoantes.

consoantes=[0,0,0,0,0,0,0,0,0,0]

for i in range(1,10):
    consoantes[i] = str(input("Digete alguma letra da matriz: "))


letra = str(input("Digete uma cosoante para localizar na matriz: "))
encontrado = False

for i in range(1,10):
    if consoantes[i] == letra:
        print("A letra encontrada", letra)
        encontrado = True

if encontrado is False:
    print("Nao tem essa cosoante")

for i in range (1,10):
    if consoantes[i] !="u" and \
            [i]  !="o" and consoantes[i] !="i" and consoantes[i] !="e" and consoantes[i] !="a":
        print(consoantes[i])
