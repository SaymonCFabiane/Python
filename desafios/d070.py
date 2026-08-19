p = 0
caro = 0
barato = 0
pro_bara = ''
cp = 0
total_gasto = 0
c = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))

    total_gasto += preco

    if preco > 1000:
        c += 1

    if cp < 1:
        barato = preco
        pro_bara = nome
    if preco < barato:
        barato = preco
        pro_bara = nome
    

    pergunta = str(input('Continuar? [S/N]')).strip().upper()
    if pergunta != 'S':
        break
    cp += 1


print(f'Ó total gasto na compra foi R${total_gasto}')
print(f'{c} produtos custam mais de R$1000.00')
print(f'O produto mais caro é {pro_bara} e custa {barato}')
