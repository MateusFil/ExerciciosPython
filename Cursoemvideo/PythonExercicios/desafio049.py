#TABUADA V2
for multiplicando in range(1, 11):
    print('Tabuada do {}'.format(multiplicando))

    for multiplicar in range(1, 11):
        resultado = multiplicando * multiplicar
        print('{} X {} = {}'.format(multiplicando, multiplicar, resultado))
