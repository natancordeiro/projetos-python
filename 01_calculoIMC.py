from time import sleep

print('\033[34m-='*14)
print('        CALCULO IMC')
print('-='*14, '\033[m')
sleep(1.3)

peso = float(input('Peso: '))
sleep(0.4)
altura = float(input('Altura: '))
sleep(0.4)
print('Calculando...')
sleep(2)
imc = peso / (altura*altura)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está \033[31mABAIXO DO PESO!\033[m')
elif 18.5 <= imc < 25:
    print('Você está no \033[32mPESO IDEAL!\033[m')
elif 25 <= imc < 30:
    print('Você está no \033[33mSOBREPESO!\033[m')
elif 30 <= imc < 40:
    print('você está no quadro de \033[31mOBESIDADE!\033[m')
elif imc > 40:
    print('Você está no quadro de \033[31mOBESIDADE MÓRBIDA!\033[m')
