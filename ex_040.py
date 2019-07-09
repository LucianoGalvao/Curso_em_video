n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print('Tirando {} e {}, a média do aluno é {:.1f}'.format(n1, n2, media))

if media < 5:
    print('O aluno foi reprovado!')
elif media > 7:
    print('O aluno está aprovado!')
else:
    print('O aluno está em recuperação!')