c = s = 0

while True:
    num =int(input('Digite um número: '))
    if num == 999:
        break
    s += num
    c += 1
print(f'Foram digitados {c} números e a soma entre eles é: {s}')
