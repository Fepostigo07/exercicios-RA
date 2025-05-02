s = float(input('Insira o valor do seu salário: '))
t = float(input('Insira o seu tempo de serviço: '))

if t>5:
    b = s*0.05
    sb = s+b
    print(f'O valor do seu salário com o bônus é {sb}')
else:
    print('Você não tem direito ao bônus')