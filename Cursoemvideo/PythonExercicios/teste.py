peso = float(input('Digite o seu peso '))
altura = float(input('Digite a sua altura '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso seu IMC é {:.1f} '.format(imc))
elif imc <= 25:
    print('PESO IDEAL IMC {:.1f}'.format(imc))
elif imc <= 30:
    print('Sobrepeso {:.1f}'.format(imc))
elif imc <= 40:
    print('Obesidade {:.1f}'.format(imc))
else:
    print('OBESIDADE MÓRBIDA')
