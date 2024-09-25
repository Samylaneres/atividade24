# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.

soma, contador = 0, 0

while (número := float(input("Digite um número"))) -1:
    soma += número
    contador += 1

media = soma / contador if contador else 0 
print("A média é:" , media)

