peso = float(input('Informe o seu peso '))
altura = float(input('Informe a sua altura '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('SEU IMC É {:.1f} RESULTADO: ABAIXO DO PESO'.format(imc))
elif imc < 25:
    print('SEU IMC É {:.1f} RESULTADO: PESO IDEAL'.format(imc))
elif imc < 30:
    print('SEU IMC É {:.1f} RESULTADO: SOBREPESO'.format(imc))
elif imc < 40:
    print('SEU IMC É {:.1f} RESULTADO: OBESIDADE'.format(imc))
else:
    print('SEU IMC É {:.1f} RESULTADO: OBESIDADE MÓRBIDA'.format(imc))
