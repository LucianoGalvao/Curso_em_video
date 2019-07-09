from datetime import date

ano_nasc = int(input('Por favor, digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - ano_nasc
alistamento = 18
print('Quem nasceu em {} tem {} anos em {}!'.format(ano_nasc, idade, ano))

if idade < alistamento:
    print('Você ainda precisará se alistar daqui {} anos em {}.'.format(18 - (idade), ano + (alistamento - idade)))
elif idade == alistamento:
    print('Esse ano você deverá se alistar!')
else:
    print('Você já passou do tempo de se alistar há {} anos em {}'.format(idade - 18, ano - (idade - 18)))