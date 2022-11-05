# Tabela de preços de pães

preço = float(input("Preço do pão: "))
print("Panificadora Pão De Cada Dia - Tabela de preços")
for i in range(1, 50+1):
    if i == 1:
        print("Preço de 1 pão - R$", preço)
    else:
        print("Valor de", i, "pães - R$", round(preço, 2))

