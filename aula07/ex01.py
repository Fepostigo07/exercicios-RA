l1 = []
acima = []
abaixo = []
for i in range (6):
    n = int(input(f'Digite o {i+1}º número: '))
    l1.append(n)
media = sum(l1)/len(l1)
for n in l1:
    if n >= media:
        acima.append(n)
    else:
        abaixo.append(n)

print(f'Média: {media}')
print(f'Números acima ou igual a média: {acima}')
print(f'Números abaixo da média: {abaixo}')
