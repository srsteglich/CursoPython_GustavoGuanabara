# Calcular com desconto
valor = float(input('Digite o valor para pagamento: R$ '))
print(''' Escolha o tipo de pagamento:
[ 1 ] À vista: Dinheiro com 10% de desconto
[ 2 ] À vista: Cartão com 5% de desconto
[ 3 ] Em 2x no cartão, preço normal
[ 4 ] Em 3x ou mais no cartão, 20% de juros''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    valor = valor - (valor * 0.1)
    print('O pagamento à vista é R$ {:.2f}, em dinheiro.'.format(valor))
elif opcao == 2:
    valor = valor - (valor * 0.05)
    print('O pagamento à vista é R$ {:.2f}, no cartão.'.format(valor))
elif opcao == 3:
    valorp = valor / 2
    print('O pagamento é R$ {:.2f} e em duas vezes é R$ {:.2f}, no cartão.'.format((valor), (valorp)))
else:
    parc = int(input('Quantas parcelas: '))
    valor = (valor * 0.2) + valor
    valorp = float(valor / parc)
    print('O pagamento será R$ {:.2f} em {} vezes.'.format((valorp), (parc)))
