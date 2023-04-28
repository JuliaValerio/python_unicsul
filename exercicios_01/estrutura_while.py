somaDasNotas = 0
qtdAlunos = 0
escolha = 'S'

while escolha == 'S':
    nota = int(input(f"Digite a nota do aluno {qtdAlunos + 1}: "))
    somaDasNotas += nota
    qtdAlunos += 1
    escolha = str(input("Deseja continuar? S/N "))
    if escolha != "S" and escolha != "s" and escolha != "N" and escolha != "n":
        print("Opção inválida. Digite 'S' para continuar ou 'N' para sair.")
        escolha = 'S'

mediaDasNotas = somaDasNotas / qtdAlunos
print(f"A média das notas é: {mediaDasNotas:.2f}")


