'''for c in range(1,10):
    print(c)
print('Fim!')
'''
'''
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim!')
'''
'''
n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('Fim!')
'''
'''
r = 'S'
while r in 'Ss':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? '))
print('Fim!')
'''
p = 0
i = 0
n = 1
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0 and n != 0:
            p += 1
        else:
            i += 1
print(f'Tivemos {p} números pares e {i} números impares!')
