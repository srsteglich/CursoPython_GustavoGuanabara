# Condições para três retas formarem um triângulo
'''
Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que
a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.

a, b e c são os lados do triângulo.
    | b - c | < a < b + c,   | a - c | < b < a + c,   | a - b | < c < a + b
'''

print('Digite os valores dos comprimentos de reta: ')
a = float(input('Reta 1 (r1): '))
b = float(input('Reta 2 (r2): '))
c = float(input('Reta 3 (r3): '))

if abs(b - c) < a < (b + c) or abs(a - c) < b < a + c or abs(a - b) < c < a + b:
    print('As retas r1 = {}, r2 = {} e r3 = {} formam um triângulo. '.format(a, b, c))
else:
    print('As retas r1 = {}, r2 = {} e r3 = {} não formam um triângulo! '.format(a, b, c))






