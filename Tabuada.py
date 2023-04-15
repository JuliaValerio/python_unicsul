# numero = int(input("Escreva o numero para saber a sua tabuada: "))
#
# for x in range(10):
#   print("O resultado de",numero, "x", x,"=", numero*x)

sequencias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for result in range(1, 11):
  for sequencia in sequencias:
    print("O resultado de", sequencia, "x", result, "=", sequencia * result)
    if sequencia == 10:
      print("----------------------------------------------------");