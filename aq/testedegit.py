
l = 0
b = 0
d = 0
branco = 0

for i in range(5):
    votacao = input(
        '\nDigite seu voto:'
        '\n1 - Lula'
        '\n2 - Bolsonaro'
        '\n3 - Diva'
        '\n4 - Branco'
        '\nAqui: '
    )

    if votacao == '1':
        l += 1
    elif votacao == '2':
        b += 1
    elif votacao == '3':
        d += 1
    elif votacao == '4':
        branco += 1
    else:
        print('Voto invalido!')

print('\n--- RESULTADO DA VOTACAO ---')
print(f'Lula: {l} votos')
print(f'Bolsonaro: {b} votos')
print(f'Diva: {d} votos')
print(f'Brancos: {branco} votos')
