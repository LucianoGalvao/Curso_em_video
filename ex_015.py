dias = int(input("Quantos dias foi alugado? "))
valor_dias = dias * 60
km = float(input("Quantos KMs rodou? "))
valor_km = km * 0.15

valor_aluguel = valor_dias + valor_km

print("Após {} dias e {} kms rodados, o valor do aluguel é de R${:.2f}.".format(dias, km, valor_aluguel))