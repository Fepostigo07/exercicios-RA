print('Insira os lados de um triângulo')
l1 = float(input('Insira o valor do primeiro lado: '))
l2 = float(input('Insira o valor do segundo lado: '))
l3 = float(input('Insira o valor do terceiro lado: '))

if l1 == l2 == l3:
    print('O triângulo é equilatero')
elif l1 == l2 or l2 == l3 or l1 == l3:
    print('O triângulo é isósceles')
else:
    print('O triângulo é escaleno')