texto = input('Digite uma palavra: ').upper()
a = texto.count('A')
e = texto.count('E')
i = texto.count('I')
o = texto.count('O')
u = texto.count('U' )
print(f'A palavra {texto} contém: ')
if a > 0:
    print(f'{a} letras A')
if e > 0:
    print(f'{e} letras E')
if i > 0:
    print(f'{i} letras I')
if o > 0:
    print(f'{o} letras O')
if u > 0:
    print(f'{u} letras U')
