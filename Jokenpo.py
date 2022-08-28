#PEDRA PAPEL E TESOURA

import random
from time import sleep
print('¨'*30)
print('Seja bem vindo ao Jokenpô 2.0!')
print('¨'*30)
print()

vitorias = 0
while True:
    print(f'Vitórias: {vitorias}')
    jogador = str(input('Você escolhe pedra, papel ou tesoura? ')).capitalize()
    maq = ['Pedra', 'Papel', 'Tesoura']
    maq = random.choice(maq)
    print('Jo...ken...pô!')
    sleep(1.0)
    print()
    print('\033[1;35mVocê\033[m escolheu \033[1;35m{}\033[m e a \033[1;34mMáquina\033[m escolheu \033[1;34m{}\033[m!'.format(jogador, maq))

    if maq == 'Pedra' and jogador == 'Papel' or maq == 'Tesoura' and jogador == 'Pedra' or maq == 'Papel' and jogador == 'Tesoura':
        print('\033[1;32mVOCÊ VENCEU!\033[m')
        vitorias += 1
        print()
        print(f'Você tem {vitorias} vitórias até aqui!')
        print()

    elif jogador == maq:
        print('\033[1mHOUVE UM EMPATE\033[m')
        print()
        print(f'Você tem {vitorias} vitórias até aqui!')
        print()

    else:
        print('\033[1;31mA MÁQUINA VENCEU!\033[m')
        print()
        print(f'Você tem {vitorias} vitórias até aqui!')
        print()

    repetir = input('Quer jogar novamente? [s/n]: ').lower()

    if repetir == 's':
        print('Se prepare!')
        sleep(0.5)
        print()
        continue
    else:
        print('Volte quando quiser se destrair um pouco! :)')
        break
