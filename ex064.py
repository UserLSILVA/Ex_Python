núm = cont = soma = 0

núm = int(input('Digite um número [999 para "stopar"]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para "stopar"]: '))
print('Você digitou {} números e a soma entre les foi {}.'.format(cont, soma))
