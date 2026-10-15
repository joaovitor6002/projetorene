l = 0
b = 0
d = 0
branco = 0
while True:
    votacao = input('\ndigite o seu voto:' '\nexistem essas tres opçoes: \n1- lula \n2- bolsonaro \n3- diva \n4- branco \naqui:')
    votacao = votacao.lower()
    if votacao == 1:
        l += 1
    elif votacao == 2:
        b += 1
    elif votacao == 3:
        d += 1
    elif votacao == 4:
        branco += 1
    else:
        print('\nvoto invalido, se quiser voltar para o menu digite 0')
        break

print(f'\nO total de votos para lula foi de: {l}')
print(f'\nO total de votos para bolsonaro foi de: {b}')
print(f'\nO total de votos para diva foi de: {d}')
print(f'\nO total de votos para branco foi de: {branco}')
