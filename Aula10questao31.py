QKm = int(input('Digite quanto KM tem o destino '))
if QKm >= 200:
    QKm = (QKm * 0.45)
    print('O Valor da passagem é R${}'.format(QKm))
else:
    QKm = (QKm * 0.50)
    print('O Valor da passagem é R${}'.format(QKm))


