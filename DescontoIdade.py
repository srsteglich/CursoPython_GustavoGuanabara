from datetime import date
atual = date.today().year
nasci = int(input('Em que ano nasceu: '))
idade = atual - nasci
cartao = input('Têm cartão da farmacia: (S)im ou (N)ão ')
valor = int(input('O valor total da compra: '))
if cartao == 'N' or 'n':
    if idade > 70:
        desc = valor - (valor * 0.07)
        print('A idade do cliente tem {} anos...'.format(idade))
        print('O valor total é: R${:.2f}, e o valor com desconto é: R${:.2F}'.format(valor, desc))
    elif 70 > idade >= 55:
        desc = valor - (valor * 0.05)
        print('A idade do cliente tem {} anos...'.format(idade))
        print('O valor total é: R${:.2f}, e o valor com desconto é: R${:.2F}'.format(valor, desc))
    else:
        print('A idade do cliente tem {} anos...'.format(idade))
        print('O valor total é: R${:.2f}'.format(valor))
else:           # Essa decisão é que o Cliente tem cartão.
    if idade > 70:
        desc = valor - (valor * 0.12)
        print('A idade do cliente tem {} anos...'.format(idade))
        print('O valor total é: R${:.2f}, e o valor com desconto é: R${:.2F}'.format(valor, desc))
    elif 70 > idade >= 55:
        desc = valor - (valor * 0.10)
        print('A idade do cliente tem {} anos...'.format(idade))
        print('O valor total é: R${:.2f}, e o valor com desconto é: R${:.2F}'.format(valor, desc))
    else:
        desc = valor - (valor * 0.05)
        print('A idade do cliente tem {} anos...'.format(idade))
        print('O valor total é: R${:.2f}, e o valor com desconto é: R${:.2F}'.format(valor, desc))
