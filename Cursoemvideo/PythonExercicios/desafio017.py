import math
cateto_oposto = float(input('Digite o valor '))
cate_adjacente = float(input('Digite o valor '))

hipotenusa = math.sqrt(cateto_oposto ** 2 + cate_adjacente ** 2)
print('A hipotenusa é {:.2f}'.format(hipotenusa))