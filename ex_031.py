distancia = int(input('Qual a distância do seu destino? '))
if distancia <= 200:
    valor1 = distancia * 0.50
    print('O valor da sua passagem, é de R${:.2f}.'.format(valor1))
else:
    valor2 = distancia * 0.45
    print('O valor da sua passagem será de R${:.2f}.'.format(valor2))
