# Binario - Octal  - Hexa
deci = int(input('Digite um numero decimal: '))
escolhe = int(input('Escolha o numero, 1 para Binário, 2 para Octal e 3 para Hexa: '))

if escolhe == 1:
    print('O {} do Decimal para Binario é {}.'.format(deci, bin(deci).strip('0b')))
elif escolhe == 2:
    print('O {} do Decimal para Octal é {}.'.format(deci, oct(deci).strip('0o').upper()))
elif escolhe == 3:
    print('O {} do Decimal para Hexa é {}.'.format(deci, hex(deci).strip('0x').upper()))
else:
    print('Digitou errado')
