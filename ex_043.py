altura = float(input('Informe seu altura: '))
peso = float(input('Informa sua peso: '))

imc = peso / (altura * altura)
print('{:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO.')
elif imc <= 25:
    print('Você está no PESO IDEAL.')
elif imc <= 30:
    print('Você está com SOBREPESO.')
elif imc <= 40:
    print('Você está com OBESIDADE.')
else:
    print('Você está com OBESIDADE MORBIDA.')