'''n1 = int(input('Digite um número '))
n2 = int(input('Digite um número '))
n3 = int(input('Digite um número '))
maior = menor = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

if n2 < menor:
  menor = n2

if n3 < menor:
    menor = n3

print('O maior numero é', maior)
print('O menor numero é ', menor)'''

a = int(input('Digite um número '))
b = int(input('Digite um número '))
c = int(input('Digite um número '))

menor = maior = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor foi {}'.format(menor))

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior é igual a : {}'.format(maior))

