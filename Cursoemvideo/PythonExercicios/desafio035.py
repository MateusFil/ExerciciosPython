""""print('Digite os comprimentos dos três lados do triângulo:')
a = float(input('Comprimento lado 1: '))
b = float(input('Comprimento lado 2: '))
c = float(input('Comprimento lado 3: '))

if a + b > c and a + c > b and b + c > a:
    print('Estes comprimentos podem ser um triângulo')
else:
    print('Não podem formar um triângulo')"""""

r1 = float(input('Digite o comprimento r1: '))
r2 = float(input('Digite o comprimento r2: '))
r3 = float(input('Digite o comprimento r3: '))

if r1 < r2 + r3 and r1 < r3 + r2 and r3 < r2 + r1 and r2 < r1 + r3:
    print('Estes comprimentos podem formar um triangulo')
else:
    print('Não é um triângulo ')