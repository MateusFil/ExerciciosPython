n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('O primeiro valor {} é maior que o segundo valor {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor {} é maior que o primeiro valor {}'.format(n2, n1))
else:
    print('Não existe valor maior, os dois são iguais: {} e {}'.format(n1, n2))
