from time import sleep

print('\033[36m-='*20)
print('      CALCULADORA INTELIGENTE')
print('-='*20, '\033[m')
sleep(1.3)

num1 = int(input('Primeiro valor: '))
sleep(.3)
num2 = int(input('Segundo valor: '))
sleep(.3)
resultado = 0
opcao = 0
while opcao != 5:
    opcao = int(input('''
[ 1 ] Somar
[ 2 ] multiplicar 
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Qual é a sua opção: '''))

    if opcao == 1:
        sleep(.8)
        print('Calculando...')
        sleep(1.3)
        resultado = num1 + num2
        print(' {} + {} = \033[1;32m{}\033[m'.format(num1, num2, resultado))
        print('=-'*10)
        sleep(2.5)
    elif opcao == 2:
        sleep(.8)
        print('Calculando...')
        sleep(1.3)
        resultado = num1 * num2
        print('{} x {} = \033[1;32m{}\033[m'. format(num1, num2, resultado))
        print('=-'*10)
        sleep(2.5)
    elif opcao == 3:
        sleep(.8)
        print('Calculando...')
        sleep(1.3)
        if num1 > num2:
            resultado = num1
        else:
            resultado = num2
        print('O maior número entre {} e {} é o \033[1;32m{}\033[m'.format(num1, num2, resultado))
        print('=-'*10)
        sleep(2.5)
    elif opcao == 4:
        print('\033[34m---Novos números---\033[m')
        sleep(.8)
        num1 = int(input('Primeiro valor: '))
        sleep(.3)
        num2 = int(input('Segundo valor: '))
        sleep(.3)
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('\033[31mOpção inválida! Tente novamente...\033[m')
        sleep(1.5)

sleep(2.5)
print('\033[1;32mPROGRAMA FINALIZADO\033[m')
