s = float(input('Digite seu salário: '))

if s <= 20000:
    print('O valor da alíquota é de R$ 0')
elif s > 20000 and s < 50000:
    a = s*0.15
    print(f'O valor da alíquota é de R$ {a}')
else:
    a = s*0.25
    print(f'O valor da alíquota é de R$ {a}')