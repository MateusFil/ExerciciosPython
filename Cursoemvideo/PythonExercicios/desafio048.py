#SOMA IMPARES MULTIPLOS DE 3
co = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        co += c

print('\nA soma de todos os {} valores é {}\n'.format(cont, co))
