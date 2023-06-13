nome = input('Digite o nome completo ')

print('O nome com letra maisculas: {} '.format(nome.upper()))
print('O nome com letra misculas: {} '.format(nome.lower()))

nomesem = nome.replace(' ', '')
print('Quantas letras sem espacos: {} '.format(len(nomesem)))
divi= nome.split()
print('Quantas letras o primeiro nome: {} '.format(len(divi[0])))


print('Outros testes....')
qtesp = nome.count(' ')
qtletra = len(nome)
semesp = qtletra - qtesp
print('Quantas letra tem o teu nome', semesp)
dividido = nome.split()
print('Quantas letra tem teu primeiro nome', len(dividido[0]))
