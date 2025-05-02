for num in range(2, 101):
    contador = 0
    for i in range(2, num):
        if num % i == 0:
            contador = contador + 1
        if contador > 0:
            print (f'{num} é número não primo.')
        else:
            print (f'{num} é número primo.')