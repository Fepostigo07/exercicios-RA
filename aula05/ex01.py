import math
a = int(input('Insira o valor de a: '))
b = int(input('Insira o valor de b: '))
c = int(input('Insira o valor de c: '))

d = (b**2)-4*a*c
if d<0:
    print('A equação não tem um valor no conjuto dos números Reais')
else:
    x1 = (-b+math.sqrt(d)/(2*a))
    x2 = (-b+math.sqrt(d)/(2*a))
    print(f'Os resulatdos da equação são {x1} e {x2}')
