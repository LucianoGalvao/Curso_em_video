numero = int(input("Digite um número de 0 a 9999: "))
num = str(numero)
print("Analisando o número {}".format(numero))
print("Unidades: {}".format(num[3]))
print("Dezenas: {}".format(num[2]))
print("Centenas: {}".format(num[1]))
print("Milhar: {}".format(num[0]))