frase = str(input('Digite uma frase: '))
frase = frase.replace(' ', '')
polindromo = frase[::-1]
if frase == polindromo:
    print('É um polindromo')
else:
    print('Não é um polindromo')

