# Leia data de nascimento
n1 = float(input('Digite a primeira nota:') )
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) /2

if media >= 7:
    print('Parabéns, está Aprovado, a media é {}.'.format(media))
elif media < 5:
    print('Reprovou direto, a tua media é {}.'.format(media))
else:
    print('Recuperação, precisa estudar mais, a media é {].'.format(media))
