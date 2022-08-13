from time import sleep

print('\033[33m-='*12)
print('        TABUADA')
print('-='*12, '\033[m')
sleep(1.3)

while True:
    n = int(input('Quer ver a tabuada de qual valor? [0 PARA SAIR] '))
    if n <= 0:
        break
    sleep(.4)
    print('Calculando...')
    sleep(1.3)
    print('-' * 15)
    for m in range(0, 10):
        m += 1
        r = n * m

        print(f'{n} X {m} = {r}')
    print('-'*15)
    sleep(3)
sleep(.7)
print('Finalizando...')
sleep(1.7)
print('\033[1;32mPROGRAMA ENCERRADO\033[m')
