from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção =0

while opção !=5:
    print('''    [1] Somar;
    [2] Multiplicar;
    [3] Maior;
    [4] Novos números;
    [5] Sair do programa.''')
    opção = int(input('>>>> Digite sua opção: '))

    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))

    elif opção == 2:
        vezes = n1* n2
        print('A multiplicação entre {} x {} é {}.'.format(n1, n2, vezes))

    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print ('Entre {} e {} o maior é {}'.format(n1, n2, maior))

    elif opção == 4:
        print ('Informe os novos valores:')
        n1 = int(input('Primeiro novo valor: '))
        n2 = int(input('Segundo novo valor: '))

    elif opção ==5:
        print('Finalizando..')

    else:
        print('Opção inválida, tente novamente!')

    print('=-=' * 10)
    sleep(1)
print('Fim do Programa! Volte sempre!')

