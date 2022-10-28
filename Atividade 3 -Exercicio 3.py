# Calculadora
fim = "s"
while fim == "s":
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))


    resultado = num1 + num2
    resultado1 = num1 - num2
    resultado2 = num1 * num2
    resultado3= num1 / num2

    print("A soma do numero 1 + numero 2 e: ", resultado)
    print("A subtração do numero 1 - numero 2 e: ", resultado)
    print("A multiplicação do numero 1 * numero 2 e: ", resultado)
    print("A divisao do numero 1 / numero 2 e: ", resultado)
    print("O resto da divisao de numero 1 / numero 2 e: ", resultado)
    print("A potencia de numero 1 pelo numero 2 e: ", resultado)

    sim = input("Deseja continuar? Sim ou Não ").upper()
    não = int(input("Fim"))

print("fim")