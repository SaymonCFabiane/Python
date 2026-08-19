from datetime import date

ma=0
me=0
atual = date.today().year

for i in range(1,8):
    anonasc = int(input(f'Em que ano a {i} pessoa nasceu: '))
    if atual - anonasc < 21:
        me += 1
    else:
        ma += 1

print(f'{ma} atingiram a maioridade!')
print(f'{me} ainda não atingiram a maioridade!')
