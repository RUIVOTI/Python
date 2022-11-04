# Casal De Coelhos

def fibonacci(meses):
    if meses >0 and meses < 3:
        return 1
    else:
        return fibonacci(meses-1)+fibonacci(meses-2)


meses = int(input("Digite o numero de meses: "))
for i in range (meses):
    casal = fibonacci(i+1)
    print("O numero de casal no mes: ", i+1, "e:",casal)