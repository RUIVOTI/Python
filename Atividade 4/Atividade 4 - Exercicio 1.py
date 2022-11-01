# Notas Do Ensino Medio

print("Notas")
B1 = float(input("Digite a nota do primeiro bimestre (Valor máximo 25): "))
B2 = float(input("Digite a nota do segundo bimestre (Valor máximo 25): "))
B3 = float(input("Digite a nota do terceiro bimestre (Valor máximo 25): "))
B4 = float(input("Digite a nota do quarto bimestre (Valor máximo 25): "))

total = float(B1 + B2 + B3 + B4)

if(total >=60 and total <=100):
    print("Você foi aprovado")
elif(total >=40 and total <60):
    print("Você esta de recuperação")
elif(total >=0 and total <40):
    print("Você foi reprovado")
else:
    print("Confira o valor digitado, valor invalido!")
