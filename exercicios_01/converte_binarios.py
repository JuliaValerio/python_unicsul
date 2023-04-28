num = input("Digite um número binário para conversão: ")
x = [int(a) for a in num]

decimal = 0
for i in range(len(x)):
    decimal += x[i] * 2**(len(x)-i-1)

print("O número decimal equivalente é:", decimal)
