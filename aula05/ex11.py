i = int(input('Digite sua idade: '))

if i >= 18:
    print('Você é maior de idade')
    if i >= 21:
        print('Você tem direito de tirar a CNH')
    else:
        print('Você não tem direito de tirar CNH')
else:
    print('Você não é maior de idade')
    