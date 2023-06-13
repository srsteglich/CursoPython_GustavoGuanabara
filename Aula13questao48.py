soma = 0
for conta in range(1, 500):
    if conta % 3 == 0:
        print(conta, end='--')
        soma = soma + conta
print('')
print('Uuuuhhhhh em multiplos de 3....')
print('A soma de todos os multipos: {}'.format(soma))
