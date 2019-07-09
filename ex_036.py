from time import sleep

print('Bem vindo ao sistema de empréstimos do Banco PyCharm!')
nome = str(input('Digite o seu nome: ')).strip().title()
print('Olá, {}! Vamos ao seu pedido de empréstimo!'.format(nome))
valor_casa = float(input('Por favor, informe o valor do imóvel: R$ '))
print('R${:.2f}'.format(valor_casa))
tempo_pgto = int(input('Informe em quantos anos será pago o imóvel: '))
meses_pgto = tempo_pgto * 12
print('{} meses'.format(meses_pgto))
parcela = float(valor_casa/meses_pgto)
print('A sua parcela, será de R$ {:.2f}'.format(parcela))
salario = float(input('Por favor, informe seu salário: R$ '))
limite = salario * .30
print('Você tem um limite de R$ {:.2f}'.format(limite))

if parcela < limite:
    print("Parabéns, {}! Seu empréstimo foi pré-aprovado!".format(nome))
    print('A parcela do seu imóvel ficará em R$ {:.2f}, sendo pago em {} meses.'.format(parcela,meses_pgto))
else:
    print('Lamentamos, mas infelizmente seu emprésimo não foi aprovado!')

print('Tenha um bom dia!')