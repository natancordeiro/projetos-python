from time import sleep

print('\033[35m-='*20)
print('     VERIFICAÇÃO DE NÚMEROS PRIMOS')
print('-='*20, '\033[m')
sleep(1.3)
numero = int(input('Digite o número que deseja verificar: '))
contador = 0
sleep(.8)
print('Verificando...')
sleep(1.2)
for index in range(1, numero+1):
    if numero % index == 0:
        print('\033[31m', end=' ')
        contador += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(index), end=' ')
sleep(1)
print('\n\033[mO número {} foi divisível {} vezes.'.format(numero, contador))
sleep(1)
if contador <= 2:
    print('Ele é um número\033[1;32mPRIMO!\033[m')
else:
    print('Ele \033[1;31mNÃO É PRIMO!\033[m')
