from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
sleep(.50)
print()
print('-='*12)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-='*12)
print()
print('JO')
sleep(.50)
print('KEN')
sleep(.50)
print('PO!!!')
print()
if computador == 0: #pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Você venceu! Papel vence pedra!')
    elif jogador == 2:
        print('O computador venceu! Pedra vence tesoura!')
    else:
        print('Jogada inválida!')

elif computador == 1: #papel
    if jogador == 0:
        print('O computador venceu! Papel vence pedra!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Você venceu! Tesoura vence papel!')
    else:
        print('Jogada inválida!')

elif computador == 2: #tesoura
    if jogador == 0:
        print('Você venceu! Pedra vence tesoura!')
    elif jogador == 1:
        print('O computador venceu! Tesoura vence papel!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')
