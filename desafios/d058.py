import random as rd
aleatorio = rd.randint(1, 10)
num = 6
tentativas = 0
while aleatorio != num:
    num = int(input('Digite um número entre 0 e 10: '))
    tentativas += 1
print(f'Parabens voce acertou, mas precisou de {tentativas} tentativas')
