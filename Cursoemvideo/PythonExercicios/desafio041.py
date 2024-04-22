import datetime
an_nascimento = int(input('Informe seu ano de nascimento '))
idade = datetime.date.today().year - an_nascimento

if idade < 9:
    print('Você tem {} anos é um atleta MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos é um atleta INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos é um atleta JÚNIOR'.format(idade))
elif idade <= 25:
    print('Você tem {} anos é um atleta SÊNIOR'.format(idade))
else:
    print('Você tem {} anos é um atleta MASTER'.format(idade))
