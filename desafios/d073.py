times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Fluminense', 'Botafogo', 'Vasco da Gama', 'São Paulo', 'Corinthians', 'Grêmio', 'Bragantino', 'Atlético-MG', 'Ceará SC', 'Internacional', 'Santos', 'EC Vitória', 'Fortaleza', 'Juventude', 'Sport Recife')

bra = times.index('Bragantino')
colo = bra + 1

print(f'A) Os 5 primeiro colocados são {times[:5]}')
print(f'B) Os ultimos 4 colocados são {times[-4:]}')
print(f'C) Os times em ordem alfabetica são {sorted(times)}')
print(f'D) O Time Bragantino está na {colo}˚ colocação')
