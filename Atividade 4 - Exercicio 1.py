# Notas Do Ensino Medio

print("Notas")
B1 = float(input("Digite a nota do primeiro bimestre: "))
B2 = float(input("Digite a nota do segundo bimestre: "))
B3 = float(input("Digite a nota do terceiro bimestre: "))
B4 = float(input("Digite a nota do quarto bimestre: "))

total = float(B1 + B2 + B3 + B4)
if(total >=60 and total <=100):
    print("Você foi aprovado")
elif(total >=40 and total <60):
    print("Você esta de recuperação")
elif(total >=0 and total <40):
    print("Você foi reprovado")
