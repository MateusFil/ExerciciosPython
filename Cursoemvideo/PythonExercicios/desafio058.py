import random

computador = random.randint(0, 10)
print('Sou o seu computador acabei de pensar um número de 0 a 10. ')
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Digite um número de 0 a 10: '))
    palpites += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais')
        elif jogador > computador:
            print('Menos')

print('Você acertou com {} palpites o número era {}'.format(palpites, computador))

