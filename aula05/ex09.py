n = float(input('Digite a sua nota: '))

if n >= 9:
    print('Sua classificação é A')
elif n >= 7 and n<9:
    print('Sua classificação é B')
elif n >= 5 and n<7:
    print('Sua classificação é C')
else:
    print('Sua classificação é D')