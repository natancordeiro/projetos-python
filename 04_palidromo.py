from time import sleep

print('\033[34m-='*20)
print('        DETECTOR DE PALÍDROMO')
print('-='*20, '\033[m')
sleep(1.3)
fr = str(input('Qual frase deseja verificar: ')).strip().upper()
palavra = fr.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
sleep(1)
print('Verificando...')
sleep(2)
print('O inverso de \033[1;33m{}\033[m é \033[1;33m{}\033[m'.format(junto, inverso))
if inverso == junto:
    print('\033[1;32mTemos um palídromo!\033[m')
else:
    print('\033[1;31mA frase não é um palídromo!\033[m')
