num = int(input('Digite um numero: '))
numr = num%2
if numr == 0:
    print('Esse numero {} é Par, pois o resto {} '.format(num, numr))
else:
    print('Esse numero {} é Impar, pois o resto {}'.format(num, numr))


