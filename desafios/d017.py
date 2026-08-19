from math import hypot
catetoOposto = float(input('Digite o cateto oposto: '))
catetoAdjacente = float(input('Digite o acteto adjacente: '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)
print(f'A hipotenusa é: {hipotenusa:.2f}')
