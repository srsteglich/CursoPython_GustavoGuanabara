# Jogo de Jokenpô
from random import randint  # numero aleatorios
from time import sleep      # tempo de espera
itens = ('Pedra', 'Papel', 'Tesoura')
cpu = randint(0, 2) # quantidade de numero 0,1,2

print(''' Opções do Jogo
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
opcao = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-=' * 11)
print('O CPU escolheu {}'.format(itens[cpu]))
print('O Jogador jogou {}'.format(itens[opcao]))
print('-=' * 11)

if cpu == 0:  # O CPU jogou Pedra
    if opcao ==0:
        print('EMPATE')
    elif opcao ==1:
        print('JOGADOR VENCE')
    elif opcao == 2:
        print('O CPU VENCE')
    else:
        print('A jogada é invalida')
elif cpu == 1:  # O CPU jogou Papel
    if opcao == 0:
        print('O CPU VENCE')
    elif opcao == 1:
        print('EMPATE')
    elif opcao == 2:
        print('JOGADOR VENCE')
    else:
        print('A jogada é invalida')
elif opcao == 2:  # O CPU jogou Tesoura
    if opcao == 0:
        print('JOGADOR VENCE')
    elif opcao == 1:
        print('O CPU VENCE')
    elif opcao == 2:
        print('EMPATE')
    else:
        print('A jogada é invalida')
#else:
#    print('TESTE A jogada é invalida')

