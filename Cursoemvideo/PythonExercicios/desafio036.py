casa = float(input('Digite o valor da casa '))
sl = float(input('Digite o seu salário '))
anos = int(input('Em quantos anos pretende pagar? '))
minimo = sl * 0.3
prestacao = casa / (anos * 12)

if prestacao <= minimo:
    print('Emprestimo aprovado {:.2f}'.format(prestacao))
else:
    print('Emprestimo negado {:.2f}'.format(minimo))


