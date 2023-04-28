valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 200:
    valor_com_desconto = valor_compra * 0.8
    print("O valor da compra com desconto é de R$", valor_com_desconto)
else:
    print("O valor da compra é de R$", valor_compra)
