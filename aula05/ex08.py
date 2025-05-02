i = int(input('Insira sua idade: '))

if i <= 12:
    print('Você é uma criança! ')
elif i >= 13 and i <= 17:
    print('Você é adolescente! ')
elif i>=18 and i <= 59:
    print('Você é adulto! ')
else:
    print('Você é idoso')
