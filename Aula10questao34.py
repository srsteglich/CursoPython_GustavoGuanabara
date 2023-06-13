sal = int(input('Digite um salario '))

if sal > 1250:
    sal = (sal * 0.1) + sal
    print('O salario aumentou de R$ {}'.format(sal))
else:
    sal = (sal * 0.15) + sal
    print('O salario aumentou de R$ {}'.format(sal))






