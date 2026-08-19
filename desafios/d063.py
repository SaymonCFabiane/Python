num = int(input('Digite um número: '))
i = 0
f = 0
p = 1
while i < num:
    print(f, end=' -> ')
    r = f + p
    f = p
    p = r
    i+=1
print('FIM')
