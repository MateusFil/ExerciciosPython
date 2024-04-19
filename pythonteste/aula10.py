import random
n = int(input('Digite um número de 0 a 5: '))
lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)
if escolhido == n:
    print('Você acertou digitou o numero {}'.format(n))
else:
    print('Você errou tente novamente o número era {}'.format(escolhido))

