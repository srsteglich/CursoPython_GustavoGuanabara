# Financiamento Bancario

valor = int(input('Digite o valor do imóvel: '))
sal = int(input('Digite o salario do comprador: '))
ano = int(input('Digite quantos anos vai pagar: '))

mes = ano * 12
prest = valor / mes
sal30 = sal * 0.3

if sal30 >= prest:
    print('O teu salario de 30% é R${:.2f}, pode fazer financiamento de R${:.2f}.'.format(sal30, prest))
else:
    print('O teu salario de 30% é R${:.2f}, acesso negado, não pode fazer financiamento de R${:.2f}.'.format(sal30, prest))









