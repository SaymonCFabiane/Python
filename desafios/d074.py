import random as rd

tupla = (rd.randint(0,10), rd.randint(0,10), rd.randint(0,10), rd.randint(0,10), rd.randint(0,10))
tupla_ordenada = sorted(tupla)


print(f'A listagem é {tupla}')
print(f'O maior valor é {tupla_ordenada[-1]} e o maior é {tupla_ordenada[0]}')

