QKm = int(input('Digite quanto KM por hora '))
if QKm > 80:
    QKm = (QKm - 80)*7
    print('Total da multa é R${}'.format(QKm))
else:
    print('Não foi multado')


