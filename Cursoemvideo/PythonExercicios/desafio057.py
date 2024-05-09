sexo = ""

while sexo != "M" and sexo != "F":
    sexo = str(input('Informe seu Sexo[M/F]: ')).upper()[0] .strip()
    if sexo != "M" and sexo != "F":
        print('Digite um valor válido')

print('FIM')
