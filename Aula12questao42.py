# Triangulo
A = int(input('Digite o lado A do Triangulo: '))
B = int(input('Digite o lado B do Triangulo: '))
C = int(input('Digite o lado C do Triangulo: '))

if ((A<B+C) and (B<A+C) and (C<A+B)):
    if ((A==B) and (B==C)):
        print('Triangulo Equilátero')
    else:
        if ((A==B) or (A==C) or (B==C)):
            print('Triangulo Isósceles')
        else:
            print('Triangulo Escaleno')
else:
    print('Não pode ser Triangulo')
