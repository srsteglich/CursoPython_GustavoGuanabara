# Leia peso e altura = IMC
peso = float(input('Digite teu Peso: '))
alt = float(input('Digite tua Altura: '))
IMC = peso / (alt ** 2)

if IMC <= 18.5:
    print('Abaixo do Peso, o teu IMC é {:.2f}.'.format(IMC))
elif (IMC > 18.5) and (IMC <=25):
    print('Peso Ideal, o teu IMC é {:.2f}.'.format(IMC))
elif (IMC > 25) and (IMC <=30):
    print('SobrePeso, o teu IMC é {:.2f}.'.format(IMC))
elif (IMC > 30) and (IMC <=40):
    print('Obesidade, o teu IMC é {:.2f}.'.format(IMC))
else:
    print('Obesidade Mórbida, o teu IMC é {:.2f}.'.format(IMC))
