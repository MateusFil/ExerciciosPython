"""import random
n = int(input('Digite um número de 0 a 5: '))
lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)
if escolhido == n:
    print('Você acertou digitou o numero {}'.format(n))
else:
    print('Você errou tente novamente o número era {}'.format(escolhido))"""

from random import randint
n = int(input('Digite um número de 0 a 5 '))
computador = randint(0, 5)
if n == computador:
    print('Você acertou o número sorteado é {}'.format(n))
else:
    print('Você ERROOOOOOU, o número era {}'.format(computador))




