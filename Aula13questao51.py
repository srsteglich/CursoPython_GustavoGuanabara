# Numero que é divido
# A cor amarela é divido
tot = 0
num = int(input('Digite um numero: '))
for conta in range(1, num+1):
    if num % conta == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[34m', end=' ')
    print('{}'.format(conta), end='')
print('\n\033[m0 numero {} foi divisivel {} vezes'.format(num, tot), end='')
if tot == 2:
    print('\n É primo!')
else:
    print('\n Não é primo!')