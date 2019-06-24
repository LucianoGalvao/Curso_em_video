s = float(input("Digite o valor do salário: "))
a = 15
sn = s + (s * a / 100)
print("O seu salário vai passar de R${:.2f} para R${:.2f}.".format(s, sn))