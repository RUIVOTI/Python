# Matriz de 5 linhas e 5 colunas.

lista = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0,], [0,0,0,0,0], [0,0,0,0,0]]

for i in range(5):
    for j in range(5):
        lista[i][j]=int(input("Digete um numero inteiro: "))

n1 = int(input("Digite um numero para localizar a matriz"))
encontrado = False
for i in range(5):
    for j in range(5):
        if(lista[i][j] == n1):
            print("nuemro encontrado", n1, "na posição", lista,i, j)
            encontrado = True
if(encontrado is False):
    print("Nao foi encontrado na matriz seu numero")



