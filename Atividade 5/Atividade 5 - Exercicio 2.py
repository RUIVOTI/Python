# ENEM

nome = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x = 0

def nomesenem(lista):
    if not lista:
        return []
    return (nomesenem([x for x in lista[1:] if x <  lista[0]])
            + [lista[0]] +
            nomesenem([x for x in lista[1:] if x >= lista[0]]))

for i in range(20):
     nome[i] = str(input("Digite um nome: "))

print(nomesenem(nome))


#

