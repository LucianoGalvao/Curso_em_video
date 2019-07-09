from datetime import date

ano = date.today().year

ano_nasc = int(input('Digite seu ano de nascimento: '))

idade = ano - ano_nasc


if idade <= 9:
    print('Atleta nascido em {}, {} anos pertence a categoria MIRIM.'.format(ano_nasc, idade))
elif idade <= 14:
    print('Atleta nascido em {}, {} anos pertence a categoria INFANTIL.'.format(ano_nasc, idade))
elif idade <= 19:
    print('Atleta nascido em {}, {} anos pertence a categoria JUNIOR.'.format(ano_nasc, idade))
elif idade <= 25:
    print('Atleta nascido em {}, {} anos pertence a categoria SÊNIOR.'.format(ano_nasc, idade))
else:
    print('Atleta nascido em {}, {} anos pertence a categoria MASTER.'.format(ano_nasc, idade))

