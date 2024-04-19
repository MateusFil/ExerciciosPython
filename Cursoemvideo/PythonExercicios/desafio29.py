velo = float(input('Digite a velocidade correspondente: '))
multa = velo - 80
cal = multa * 7
if velo > 80:
    print('Você recebeu uma multa e irá pagar {:.2f}'.format(cal))
else:
    ('Você está no limite da via tenha uma boa viage :)'.format(velo))