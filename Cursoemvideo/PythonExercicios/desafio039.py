import datetime

ano_nasc = int(input('Informe seu ano de nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc

if idade < 18:
    plural_ano = 's' if (18 - idade) > 1 else ''
    print('Você tem {} anos e faltam {} ano{} para você se alistar'.format(idade, 18 - idade, plural_ano))
elif idade == 18:
    print('Você tem {} anos e está no momento exato para se alistar'.format(idade))
else:
    plural_ano = 's' if (idade - 18) > 1 else ''
    print('Você tem {} anos e já se passaram {} ano{} para o alistamento'.format(idade, idade - 18, plural_ano))


 