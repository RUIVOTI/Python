# Notas Do Ensino Medio

print("Notas")
PROV1 = float(input("Digete a nota da primeiro da prova: "))
PROV2 = float(input("Digete a nota da segunda prova: "))
PROV3 = float(input("Digete a nota da terceira prova: "))
PROV4 = float(input("Digete a nota da quarta prova: "))

TRA1 = float(input("Digite a nota do primeiro trabalho: "))
TRA2 = float(input("Digete a nota do segundo trabalho: "))
TRA3 = float(input("Digete a nota do terceiro trabalho: "))
TRA4 = float(input("Digete a nota do quarto trabalho: "))

valor1 = float(PROV1 + TRA1)
valor2 = float(PROV2 + TRA2)
valor3 = float(PROV3 + TRA3)
valor4 = float(PROV4 + TRA4)

valor1 = float(valor1/2)
print("A media do primeiro bimestre", valor1)
valor2 = float(valor2/2)
print("A media do segundo bimestre", valor2)
valor3 = float(valor3/2)
print("A media do terceiro bimestre", valor3)
valor4 = float(valor4/2)
print("A media do quarto bimestre", valor4)
valortotal = valor1 + valor2 + valor3 + valor4


if(valortotal >=60 and valortotal <=100):
    print("Você foi aprovado")
elif(valortotal >=40 and valortotal <60):
    print("Você esta de recuperação")
elif(valortotal >=0 and valortotal <40):
    print("Você foi reprovado")
