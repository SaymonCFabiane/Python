n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a sua sagunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi: {m:.1f}')
if (m >= 7):
    print('Aprovado!')
else:
    print('Reprovado!')
