# media de idades
idades = 0
# homem mais velho
maioridadehomem = 0
nomevelho = ''
# mulheres abaixo de 20 anos
totmulher20 = 0

for p in range(1, 5):
    #inserção de dados
    print('----- {}ª PESSOA ----- '.format(p))
    nome = str(input('Nome: ').title().strip())
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip())
    # soma das idades
    idades += idade
    # testes para maior idade homem
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    # continuação de teste para os demais itens
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    # teste para se mulher menor de 20 anos
    if sexo in 'Ff' and idade < 20:
        totmulher20 =+ 1
mediaidade = idades / 4
print('A média de idade do grupo é {:.1f} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('São {} mulheres com menos de 20 anos.'.format(totmulher20))