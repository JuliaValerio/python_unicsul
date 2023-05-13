import calculadora

num1 = int(input("digite o primeiro numero inteiro: "))
num2 = int(input("digite o segundo numero inteiro: "))
string = input("Digite a operação que deseja fazer: [+] [-] [*] [/]")

if (string == "+"):
    print("Resultado soma")
    calculadora.soma(num1, num2)
elif (string == "-"):
    print("Resultado subtração")
    calculadora.subtracao(num1, num2)
elif (string == "/"):
    print("Resultado divisão")
    calculadora.divisao(num1, num2)
elif (string == "*"):
    print("Resultado multiplicação")
    calculadora.multiplicao(num1, num2)
elif (string == "sair"):
    print("Fim do programa :)")
    pass
else:
    print("Operação invalida!")







