escolhido = int(input('Digite um número para a conversão '))
num = int(input('Digite um número para selecionar '))
print('ESCOLHA A CONVERSÃO DE 1 A 3')
print('APERTE [ 1 ] PARA BINÁRIO')
print('APERTE [ 2 ] PARA OCTAL')
print('APERTE [ 3 ] PARA HEXADECIMAL')

if num == 1:
    print('A conversão de {} para binário é {}'.format(escolhido, bin(escolhido)))
elif num == 2:
    print('A conversão de {} para OCTAL é {}'.format(escolhido, oct(escolhido)))
elif num == 3:
    print('A conversão de {} para HEXADECIMAL É {}'.format(escolhido, hex(escolhido)))
else:
    print('Opção Inválida !!')
