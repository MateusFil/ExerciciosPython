s = float(input('Digite o valor do seu sálario '))

if s > 1250:
    print('Com o aumento de 10% seu sálario será: {:.2f}'.format(s * 1.10))
if s <= 1250:
    print('Com o aumento de 15% seu sálario será: {:.2f}'.format(s * 1.15))
