r = 'S'
s = 0
c = 0
maior = 0
antigo = 0
menor = 0
while r == 'S':
    num = int(input('Digite um número:'))
    c += 1
    maior = num
    if num > maior:
        maior = num
    if num < maior:
        menor = num
    s += num
    r = str(input('Deseja continuar se sim digite [S] se não digite [N]: ')).upper()
media = s / c
print(f'Você digitou {c} vezes')
print(f'A média é de {media}')
print(f'E o maior número é o número {maior} e o menor é {antigo}')

