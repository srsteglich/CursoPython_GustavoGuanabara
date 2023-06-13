from datetime import date
atual = date.today().year
nasci = int(input('Em que ano nasceu: '))
idade = atual - nasci
cartao = intput("Têm cartão da farmacia: (S)im ou (N)ão ")
valor = intput("O valor total da compra:" )
if cartao == N:
    if idade > 70:
        print('O valor descontado é: '.format(idade))
    elif idade <= 14:
        print('O atleta tem {} anos, então é INFANTAL. '.format(idade))
    elif idade <= 19:
        print('O atleta tem {} anos, então é JUNIOR. '.format(idade))
    elif idade <= 25:
        print('O atleta tem {} anos, então é SENIOR. '.format(idade))
    else:
        print('O atleta tem {} anos, então é MASTER. '.format(idade))
else:
