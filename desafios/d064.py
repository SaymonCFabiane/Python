i = 0
c = 0
s = 0
while i != 999:
    num = int(input('Digite um número: '))
    c += 1
    s = s + num
    i = num
print(f'Foram digitados ao todo {c - 1} números e a soma entre ele é: {s - 999}')
