import random
aleatorio = random.randint(0, 5)
num = int(input('Digite um numero de 0 a 5: '))
if num == aleatorio:
    print('Você venceu!')
else:
    print('Você perdeu!')
print(f'O numero era {aleatorio}!')
