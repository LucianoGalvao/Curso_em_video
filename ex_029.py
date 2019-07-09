velocidade = float(input("Digite a velocidade medida: "))
if velocidade > 80.0:
    multa = (velocidade - 80.0) * 7
    print("Você ultrapassou o limite de 80km/h! Sua multa será de R${:.2f}".format(multa))
print('Tenha um bom dia! Dirija com segurança!')
