pares = 0
cont = 0
for c in range(1, 7):
    if c % 2 == 0:
        pares += c
        cont += 1

print('Você informou {} números pares e a soma é {}'.format(cont, pares))

