r = float(input("Digite quantos reais você possui: R$"))
dc = 3.27
v = r/dc

print("Com R${} você pode comprar U${:.2f}.".format(r,v))