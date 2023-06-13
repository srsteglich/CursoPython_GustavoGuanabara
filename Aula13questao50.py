soma = 0
conta = 0
for c in range(1, 7):
    num = int(input('Digite o {} numeros: '.format(c)))
    if num % 2 == 0:
        soma += num
        conta += 1
print("Voce informou {} numeros e a soma foi {}". format(conta, soma))
