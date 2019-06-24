p = float(input("Digite o valor do produto: R$"))
d = p*5/100
v = p - d
print("O produto com valor de R${:.2f}, fica por R${:.2f} com 5% de desconto!".format(p,v))