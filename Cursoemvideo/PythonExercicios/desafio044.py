pagamento = float(input('Informe o valor do produto: '))
escolha = int(input('Selecione a forme de pagamento 1 a 4: '))
print('Digite [ 1 ] à vista dinheiro/cheque: 10% de desconto')
print('Digite [ 2 ] à vista no cartão: 5% de desconto')
print('Digite [ 3 ] em até 2x no cartão: preço formal')
print('Digite [ 4 ] 3x ou mais no cartão: 20% de juros')


if escolha == 1:
    total = pagamento * 0.90
if escolha == 2:
    total = pagamento * 0.95
if escolha == 3:
    total = pagamento
if escolha == 4:
    total = pagamento * 1.20
print('Total a pagar {:.2f}'.format(total))
