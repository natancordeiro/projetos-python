from random import randint
from time import sleep

par = 'PAR'
impar = 'IMPAR'
contador = 0
print('-'*25)
print('  JOGO DO PAR OU IMPAR')
print('-'*25)
sleep(1)
while True:
    num_jogador = int(input('Digite um número de 0 a 10: '))
    num_computador = randint(0, 10)

    if num_jogador % 2 == 0:
        print('Você jogou um número PAR')
        num_jogador = par
    elif num_jogador % 2 == 1:
        print('Você jogou um número IMPAR')
        num_jogador = impar
    if num_computador % 2 == 0:
        print(f'O computador jogou um número PAR ({num_computador})')
        num_computador = par
    elif num_computador % 2 == 1:
        print(f'O computador jogou um número IMPAR ({num_computador})')
        num_computador = impar
    if num_jogador != num_computador:
        break
    contador += 1
    print('\033[32mAcertou! continue...\033[m')
    sleep(1)
print(f'\033[31mVocê perdeu!\033[m\nVocê acertou \033[1;32m{contador}\033[m vezes consecutivas. Parabéns!')
