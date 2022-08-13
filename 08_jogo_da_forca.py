from time import sleep
from random import randint

# JOGO DA FORCA
print('\033[1;36m-='*12)
print('    JOGO DA FORCA')
print('-='*12, '\033[m')
sleep(1.3)

# Variáveis globais
palavras = ('perfume', 'boneco', 'garrafa', 'mochila', 'geladeira')
digitadas = []
chance = 3

while True: 
    # Verificação da palavra de uso
    sec = input('''Como deseja jogar
    [1] Criar palavra
    [2] Usar palavra aleatória
    --> ''').strip()
    if sec == '1':
        secreto = input('Qual a palavra deseja usar? ')
        sleep(1)
        print('\033[1;32mPalavra salva!\033[m')
        sleep(1)
        print('Vamos jogar...')
        break
    elif sec == '2':
        secreto = palavras[randint(0,4)]
        break
    else: 
        print('\033[1;31mDigite um valor válido!\033[m')
        sleep(1)
        continue
sleep(1)
while True:
    # Contador de chances
    if chance <= 0:
        sleep(1)
        print('\033[1;31mVOCÊ PERDEU!!\033[m')
        break

    letra = input('Digite uma letra: ')
    sleep(1)

    # Teste de erro (mais de uma letra digitada)
    if len(letra) > 1:
        print('\033[1;31mERRO!! Digite apenas uma letra.\033[m')
        continue

    # Incremento da letra na variável
    digitadas.append(letra)

    # Verificação de acerto
    if letra in secreto:
        print(f'\033[1;32mVOCÊ ACERTOU, a letra "{letra}" existe na palavra secreta.\033[m')
    else: 
        print(f'\033[1;31mERROU, a letra "{letra}" NÃO EXISTE na palavra secreta.\033[m')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    
    # Verificação de Game Over
    if secreto_temporario == secreto:
        sleep(1.3)
        print(f'\033[1;32mPARABÉNS VOCÊ VENCEU!!')
        sleep(1)
        print(f'A palavra secreta era \033[1;33m{secreto_temporario} \033[m')
        break
    else: 
        sleep(1.4)
        print(f'A palavra secreta está assim: \033[1;36m{secreto_temporario}\033[m')

    # Decressão do contador de chances
    if letra not in secreto_temporario:
        chance -= 1
    sleep(1.4)
    print(f'\033[1;33mVocê tem {chance} chances.\033[m')
