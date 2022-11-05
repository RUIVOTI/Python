# Programa que leia vetores

vetor1 = []
vetor2 = []
vetor3 = []

for elemento in range(0,10):
    vetor1.append(int(input("Digite um elemento: ")))

for elemento in range(0,10):
    vetor2.append(int(input("Digite um elemento: ")))

for elemento in range(0,10):
    vetor3.append((vetor1[elemento]))
    vetor3.append((vetor2[elemento]))

print(vetor3)
print(vetor2)
print(vetor1)




