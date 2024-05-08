sexo = ""

while sexo != "M" and sexo != "F":
    sexo = str(input('Digite seu Genero[M/F]: ')).upper()
    if sexo != "M" and sexo != "F":
        print('Digite um valor válido')

print('FIM')
