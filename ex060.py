n1 = int(input('Digite um nº para calcular o seu fatorial: '))
c = n1
f = 1

print('Calculando o {}! = '.format(n1), end= '')
while c>0:
    print('{}'.format(c), end= '')
    print(' x ' if c>1 else ' = ', end='')
    f *= c
    c -=1

print('{}'.format(f))
