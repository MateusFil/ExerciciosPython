from math import radians, sin , cos, tan
angulo_graus = float(input('Digite o angulo '))
angulo_radianos = radians(angulo_graus)
seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)

print('O Seno é {:.2f} O Cosseno é {:.2f} e o Tangente :{:.2f}'.format(seno, cosseno, tangente))
