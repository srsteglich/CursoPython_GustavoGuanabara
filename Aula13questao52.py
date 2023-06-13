# Palindromo
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()     # seleciona sem espaço
junto = ''.join(palavra)    # tira espaço
inverso = ''
        #inverso = junto[::-1] tambem dá pra fazer, tirar o "For"
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
     print('Temos um Palmdromo!')
else:
     print('Não temos um Palmdromo!')
