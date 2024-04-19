nome = str(input('Digite seu nome '))
if nome == 'Mateus':
    print('Que nome bonito!!!')
elif nome == 'Ana' or 'Jessica' or 'Klaudia':
    print('Que nome feminino lindo')
elif nome in 'Maria Pedro Paulo Joao':
    print('Você tem um nome bem popular no Brasil')
print('Tenha um bom dia {}'.format(nome))