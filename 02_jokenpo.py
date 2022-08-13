from random import randint
from time import sleep

print('\033[30m-='*13)
print('        JO-KEN-PO')
print('-='*13, '\033[m')
sleep(1.3)
itens = ('Pedra 👊', 'Papel ✋', 'Tesoura ✌')
pc = randint(0, 2)
print('''Suas opções: 
[ 0 ] PEDRA 👊
[ 1 ] PAPEL ✋
[ 2 ] TESOURA  ✌''')
opcao = int(input('Qual é a sua jogada: '))
sleep(0.5)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

print('-=' * 14)
print('Você jogou {}'.format(itens[opcao]))
print('Computador jogou {}'.format(itens[pc]))
print('-=' * 14)
if pc == 0:
    if opcao == 0:
        print('\033[33mEMPATE!\033[m')
    elif opcao == 1:
        print('\033[32mVOCÊ VENCEU!\033[m')
    elif opcao == 2:
        print('\033[31mVOCÊ PERDEU!\033[m')
    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')
elif pc == 1:
    if opcao == 0:
        print('\033[31mVOCÊ PERDEU!\033[m')
    elif opcao == 1:
        print('\033[33mEMPATE!\033[m')
    elif opcao == 2:
        print('\033[32mVOCÊ VENCEU!\033[m')
    else:
        print('\033[31mJOGADA INVÁLIDA!\033[m')
elif pc == 2:
    if opcao == 0:
        print('\033[32mVOCÊ VENCEU!\033[m')
    elif opcao == 1:
        print('\033[31mVOCÊ PERDEU!\033[m')
    elif opcao == 2:
        print('\033[33mEMPATE!\033[m')
    else:
        print('\033[31mJOGADA INVÁLDA!\033[m')
else:
    print('\033[31mNÚMERO INVÁLIDO! Tente novamente....\033[m')
