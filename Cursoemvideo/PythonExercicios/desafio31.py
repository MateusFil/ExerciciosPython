dis = float(input('Digite quantos km serão percorridos '))
if dis <= 200:
    print('O total da vigem é {} km será {}'.format(dis, dis * 0.50))
else:
    print('O total da sua vigem é: {} km e o valor {}'.format(dis, dis * 0.45))