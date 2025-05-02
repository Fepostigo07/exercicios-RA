v = float(input('Insira o valor da compra: '))

if v>100:
    d = v*0.1
    vd = v - d
    print(f'O valor da compra será de {vd}')
else:
    print('Você não tem direito ao desconto')