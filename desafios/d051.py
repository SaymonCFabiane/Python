priter = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = priter + (10-1) * razao

for c in range(priter, decimo, razao):
        print(c, end=' -> ') 

print('ACABOU')
