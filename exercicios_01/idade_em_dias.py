anos = int(input("Digite a sua idade em anos: "))
meses = int(input("Digite a quantidade de meses completos desde o último aniversário: "))
dias = int(input("Digite a quantidade de dias desde o último mês completo: "))

idade_em_dias = anos * 365 + meses * 30 + dias

print("A sua idade em dias é:", idade_em_dias)
