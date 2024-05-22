sair = False

while not sair:

    print('Selecione uma operação: ')
    print('Digite [1] para soma ')
    print('Digite [2] para multiplicação')
    print('Digite [3] maior')
    escolha = str(input('Digite SAIR para encerrar o programa: ')).upper()
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))

    if escolha == 'SAIR':
        sair = True
    else:
        if escolha == '1':
            print('Soma: ')
            print('A soma entre {} + {}: {} '.format(n1, n2, n1 + n2))
        elif escolha == '2':
            print('Multiplicação: ')
            print('{} x {}: {}'.format(n1, n2, n1 * n2))
        elif escolha == '3':
            if n1 > n2:
                print('O maior número é {}'.format(n1))
            else:
                print('O maior número é {}'.format(n2))









