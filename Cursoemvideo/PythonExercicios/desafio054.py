import  datetime
maioridade = 0
menoridade = 0
atual = datetime.date.today().year
for pessoa in range(1, 8):
    ano = int(input('Em que ano a {}ª nasceu? '.format(pessoa)))
    idade = atual - ano

    if idade >= 18:
        print('Você é maior de idade {} anos'.format(idade))
        maioridade += 1

    else:
        print('Você é menor de idade {} anos'.format(idade))
        menoridade += 1

print('{} pessoas não atingiram a maioridade'.format(menoridade))
print('{} pessoas já são maiores de idade'.format(maioridade))






