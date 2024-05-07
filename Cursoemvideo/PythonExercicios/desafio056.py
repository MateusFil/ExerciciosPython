maior = 0
cont = 0
maisvelho = ''
idadecont = 0

for pessoas in range(1, 5):
    nome = input('Informe o seu nome: ')
    idade = int(input('Informe a sua idade: '))
    sexo = input('Informe o seu Sexo[M/F]: ')
    print('{}º Nome: {} Idade:{} anos Sexo[M/F]: {}'.format(pessoas, nome, idade, sexo))
    idadecont += idade

    if sexo in 'Mm' and idade > maior:
        maior = idade
        maisvelho = nome

    elif sexo in 'Ff' and idade < 20:
        cont += 1


print('Ao todo são {} mulheres com menos de 20 anos'.format(cont))
print('O homem mais velho é {} '.format(maisvelho))
print('A média de idade do grupo é {} '.format(idadecont / 4))

