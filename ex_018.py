from math import radians, cos, sin, tan

angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O ãngulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cos = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos))
tang = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tang))
