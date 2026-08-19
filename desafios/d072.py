extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


while True:

    num = int(input('Digite um número ente 0 e 20: '))

    if num > 0 and num < 21:
        break
    else:
        print('Valor invalido tente novamente', end=' ')

print(f'O número {num} em extenso é {extenso[num]}!')
