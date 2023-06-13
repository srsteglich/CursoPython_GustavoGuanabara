num = int(input('Escolha o numero para tabuada: '))

for conta in range(1, 10):
    mult = conta * num
    print(conta, 'X', num, '=', mult)
print("Feito a Tabuada....")