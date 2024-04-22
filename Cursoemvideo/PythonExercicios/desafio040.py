nota1 = float(input('Informe o primeiro resultado da prova '))
nota2 = float(input('Informe o segundo resultado da prova '))
media = (nota1 + nota2) / 2

if media < 5:
    print('SUA MÉDIA É {:.2f} RESULTADO: REPROVADO'.format(media))
elif media <= 6.9:
    print('SUA MÉDIA É {:.2f} RESULTADO: RECUPERAÇÃO'.format(media))
else:
    print('SUA MÉDIA É {:.2f} RESULTADO: APROVADO'.format(media))
