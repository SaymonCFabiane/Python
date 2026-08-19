'''
lanche_pessoal = str(input('Digite o nome de um lanche: '))
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', lanche_pessoal)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
print(len(lanche))


lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')


print(sorted(lanche))
'''
'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c)
print(c.count(4))
print(c.index(2, 2))
print(d)
'''

pessoa = ('Saymon', 19, 'M', 84.89)
del(pessoa)
print(pessoa)
