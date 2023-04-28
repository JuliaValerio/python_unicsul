valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == '+':
    resultado = valor1 + valor2
elif operacao == '-':
    resultado = valor1 - valor2
elif operacao == '*':
    resultado = valor1 * valor2
elif operacao == '/':
    resultado = valor1 / valor2
else:
    print("Operação inválida!")
    exit()

print("Resultado: ", resultado)
