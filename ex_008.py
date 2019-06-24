m = float(input("Digite uma distância em metros: "))
km = m*0.001
hm = m*0.01
dam = m*0.1
dm = m*10
cm = m*100
mm = m*1000
print("{} metros corresponde a:".format(m))
print("{}m são {} quilômetros".format(m, km))
print("{}m são {} hectõmetros".format(m, hm))
print("{}m são {:.2f} decâmetros".format(m, dam))
print("{}m são {} decímetros".format(m, dm))
print("{}m são {} centímetros ".format(m, cm))
print("{}m são {} milímetros".format(m, mm))