frase = str(input('Digite uma frase: ').upper().strip())
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}!'.format(junto, inverso))

if inverso == junto:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')
