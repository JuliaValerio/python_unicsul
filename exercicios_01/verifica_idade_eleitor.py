idade = int(input("Digite a sua idade: "))

if idade < 16:
    print("Você ainda não é eleitor.")
elif idade >= 18 and idade <= 65:
    print("Você é um eleitor obrigatório.")
else:
    print("Você é um eleitor facultativo.")
