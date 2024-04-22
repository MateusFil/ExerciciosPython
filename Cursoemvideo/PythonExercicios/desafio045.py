import random
print('Bem-vindo ao JokePO você deve escrever o atributo que irá jogar')
print('Exemplo: - Pedra  - Papel ou Tesoura :D')
escolha = str(input('JO KEN PÔ !! ')).upper()
n1 = 'PEDRA'
n2 = 'PAPEL'
n3 = 'TESOURA'

maquina = random.choice([n1, n2, n3])

if escolha == 'PEDRA' and maquina == 'PAPEL':
    print('VOCÊ JOGOU {} CONTRA {} E PERDEUUUU!!!'.format(escolha, maquina))
elif escolha == 'TESOURA' and maquina == 'PEDRA':
    print('VOCÊ JOGOU {} CONTRA {} E PERDEUUUU!!!'.format(escolha, maquina))
elif escolha == 'PAPEL' and maquina == 'TESOURA':
    print('VOCÊ JOGOU {} CONTRA {} E PERDEUUUU!!!'.format(escolha, maquina))

elif escolha == 'PEDRA' and maquina == 'TESOURA':
    print('VOCÊ JOGOU {} CONTRA {} E GANHOOOUU!!!'.format(escolha, maquina))
elif escolha == 'PAPEL' and maquina == 'PEDRA':
    print('VOCÊ JOGOU {} CONTRA {} E GANHOOOUU!!!'.format(escolha, maquina))
elif escolha == 'TESOURA' and maquina == 'PAPEL':
    print('VOCÊ JOGOU {} CONTRA {} E GANHOOOUU!!!'.format(escolha, maquina))
else:
    print('EMPATEEEEEE')











