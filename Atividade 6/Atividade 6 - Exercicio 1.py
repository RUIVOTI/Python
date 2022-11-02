# Salario

salario = int(input("Digite quanto você ganha por hora: "))
horas =  int(input("Digite o numero de horas trabalhadas no mês: "))

bruto = salario * horas
ir = (bruto - (bruto * (11/100)))
inss = (ir - (ir * (8/100)))
sindicato = (inss - (inss * (5/100)))
liquido = sindicato

print("Salario bruto: R$",bruto)
print("Salario liquido: R$",liquido)
print("Quanto pagou ao INSS: R$",bruto - ir)
print("Quanto pagou ao INSS: R$",ir - inss)
print("Quanto pagou ao Sindicato: R$",inss - sindicato)