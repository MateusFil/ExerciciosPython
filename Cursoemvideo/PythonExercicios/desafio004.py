valor = input('Digite um Valor ')
if valor.isnumeric():
    print('O valor digitado é um número ',type(valor))

elif valor.isalpha():
    print('O valor digitado é uma string ',type(valor))
else:
    print('O valor digitado é uma combinação de letras e números e etc ', type(valor))

