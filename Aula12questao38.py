num = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

if num < num2:
    print('O numero maior é {}'.format(num2))
elif num2 < num:
    print('O numero maior é {}'.format(num))
else:
    print('Numero são igual {} e {}.'.format(num, num2))
