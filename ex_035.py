r1 = float(input("Primeiro elemento: "))
r2 = float(input("Segundo elemento: "))
r3 = float(input("Terceiro elemento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Essas retas formam um triangulo!")
else:
    print('Essas retas não formam um triangulo!')