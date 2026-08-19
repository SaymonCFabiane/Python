'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 2)
print(num)
num.pop(2)
print(num)
if 4 in num:
    num.remove(4)
else:
    print(f'Não achei o númro 4!')
print(num)
print(f'Essa lista tem {len(num)} elementos')'''
'''
valores = []

print('='*40)
print(f'{"DIGITE OS VALORES!":^40}')
print('='*40)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print('='*40)
print(f'{"RESULTADOS!":^40}')
print('='*40)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')

print('='*40)
'''

'''
a = [2, 3, 4, 7]
b = a Ligação
b[2] = 8

print(a)
print(b)
'''

a = [2, 3, 4, 7]
b = a[:] 
b[2] = 8

print(a)
print(b)