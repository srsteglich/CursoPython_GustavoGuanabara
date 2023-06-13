ano = int(input('Digite Ano para Bissexto: '))
if (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0)):
    print('É Ano Bissexto')
else:
    print('Não é Ano Bissexto')

