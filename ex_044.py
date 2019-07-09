print('{:=^40}'.format('LOJAS PYCHARM'))
preco = float(input('Digite o valor do produto: R$ '))
print('Digite a forma de pagamento:')
print('''[ 1 ] À vista dinheiro/cheque(10% desconto)
[ 2 ] À vista no cartão (5% de desconto)
[ 3 ] 2x no cartão (sem juros)
[ 4 ] 3 ou mais vezes no cartão (20% de juros''')
condicao = int(input("Forma: "))
if condicao == 1:
    print('O novo valor do produto é de R$ {:.2f}'.format(preco - (preco * .10)))
elif condicao == 2:
    print('O novo valor do produto é de R$ {:.2f}'.format(preco - (preco * .05)))
elif condicao == 3:
    print('O valor permanece o mesmo de R$ {:.2f}'.format(preco))
elif condicao == 4:
    parcela = int(input('Quantas parcelas? '))
    preco_parcela = preco / parcela
    if parcela >= 3 and parcela <= 12:
        print('O novo valor do produto é de R$ {:.2f}, pago em {}x de R${:.2f}'.format(preco + (preco * 0.20), parcela,preco_parcela))
    else:
        print('Parcelamento invalido.')
else:
    print('Opção inexistente!')