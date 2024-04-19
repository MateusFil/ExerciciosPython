frase = str(input('Digite uma frase ')).strip().upper()
print('A letra "A" aparece : {} '.format(frase.count('A', 0, 90)))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1))

