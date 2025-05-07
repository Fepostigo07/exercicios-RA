l1 = []
l2 = []
l3 = []

for i in range (5):
    n1 = int(input('Digite um número: '))
    l1.append(n1)
for i in range (5):
    n2 = int(input('Digite um número: '))
    l2.append(n2)
for a, b in zip(l1, l2):
    l3.append(a)
    l3.append(b)
print(l3)