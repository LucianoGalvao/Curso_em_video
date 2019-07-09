from random import randint
from time import sleep

numero = randint(0,5)
print('-=-' * 20)
print('Estou pensando em um número de 0 até 5... Você é capaz de acertá-lo?')
print('-=-' * 20)
chute = int(input('Digite seu chute: '))

print('PROCESSANDO.')
sleep(0.5)
print('PROCESSANDO..')
sleep(0.5)
print('PROCESSANDO...')
sleep(1 )
if chute == numero:
    print('Parabéns, você acertou! Eu estava realmente pensando no número {}.'.format(numero))
else:
    print('Lamento, você errou! Eu pensei no número {} e não no número {}.'.format(numero, chute))
