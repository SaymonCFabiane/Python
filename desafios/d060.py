'''
num = int(input('Digite um número: '))
ni = num
f = num
while f != 1 and f != 0:
    num = num * (f - 1)
    f -= 1
print(f'O fatorial de {ni} é: {num}')
'''

from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print(f'O fatorial de {n} é: {f}')
