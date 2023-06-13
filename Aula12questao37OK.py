# Binario - Octal  - Hexa
deci = int(input('Digite um numero decimal: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexa''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para Binario é igual a {}.'.format(deci, bin(deci)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}.'.format(deci, oct(deci)[2:]))
elif opcao == 3:
    print('{} convertido para Hexa é igual a {}.'.format(deci, hex(deci)[2:]))
else:
    print('Opção invalida. Tente novamente.')
