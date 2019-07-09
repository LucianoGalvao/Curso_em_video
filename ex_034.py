salario = int(input('Digite seu salário: '))

if salario <= 1250.00:
    aumento = salario * 0.15
    novosalario = salario + aumento
    print('Seu aumento será de R${:.2f} e seu novo salario será de R${:.2f}.'.format(aumento, novosalario))
else:
    aumento = salario * 0.10
    novosalario = salario + aumento
    print('Seu aumento será de R${:.2f} e seu novo salário será de R${:.2f}.'.format(aumento, novosalario))