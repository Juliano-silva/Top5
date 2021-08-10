from random import randint
from time import sleep
while True:
    print('==='*10)
    itens=('Bahamut','Marilith','Tiamat')
    print('[1] Lutar contra Bahamut')
    print('[2] Lutar contra Marilith')
    print('[3] Lutar contra Tiamat')
    print('==='*10)
    opção=int(input('Escolha um monstro Para lutar: '))
    itens1=('Espada da Perdição','Arco do Julgamento','Machado do Tormento')
    print('==='*10)
    JOKER=('Tesoura', 'Pedra', 'Papel')
    print('[0] Tesoura')
    print('[1] Pedra')
    print('[2] Papel')
    Jogador=int(input('Qual é a sua rodada? '))
    print('==='*10)
    Bahamut=randint(0,2)
    Marilith=randint(0,2)
    Tiamat=randint(0,2)
    print('O Jogador Jogou {}'.format(JOKER[Jogador]))
    print('O Bahamut Jogou {}'.format(JOKER[Bahamut]))
    if opção==1:
        if Bahamut==0:
            if Jogador==0:
                print('Empate')
            elif Jogador==1:
                print('Você Ganhou')
            elif Jogador==2:
                print('Você Perdeu')
            else:
                print('Jogada Inválida')
        if Bahamut == 1:
            if Jogador == 0:
                print('Você Perdeu')
            elif Jogador == 1:
                print('Empate')
            elif Jogador == 2:
                print('Você Ganhou')
            else:
                print('Jogada Inválida')
        if Bahamut == 2:
            if Jogador == 0:
                print('Você Ganhou')
            elif Jogador == 1:
                print('Você Perdeu')
            elif Jogador == 2:
                print('Empate')
            else:
                print('Jogada Inválida')
    if opção==2:
        if Marilith==0:
            if Jogador==0:
                print('Empate')
            elif Jogador==1:
                print('Você Ganhou')
            elif Jogador==2:
                print('Você Perdeu')
            else:
                print('Jogada Inválida')
        if Marilith == 1:
            if Jogador == 0:
                print('Você Perdeu')
            elif Jogador == 1:
                print('Empate')
            elif Jogador == 2:
                print('Você Ganhou')
            else:
                print('Jogada Inválida')
        if Marilith == 2:
            if Jogador == 0:
                print('Você Ganhou')
            elif Jogador == 1:
                print('Você Perdeu')
            elif Jogador == 2:
                print('Empate')
            else:
                print('Jogada Inválida')
    if opção==3:
        if Tiamat==0:
            if Jogador==0:
                print('Empate')
            elif Jogador==1:
                print('Você Ganhou')
            elif Jogador==2:
                print('Você Perdeu')
            else:
                print('Jogada Inválida')
        if Tiamat == 1:
            if Jogador == 0:
                print('Você Perdeu')
            elif Jogador == 1:
                print('Empate')
            elif Jogador == 2:
                print('Você Ganhou')
            else:
                print('Jogada Inválida')
        if Tiamat == 2:
            if Jogador == 0:
                print('Você Ganhou')
            elif Jogador == 1:
                print('Você Perdeu')
            elif Jogador == 2:
                print('Empate')
            else:
                print('Jogada Inválida')
    C= str(input('Você quer continuar[S/N]? ')).upper().strip()[0]
    sleep(0.5)
    if C=='N':
        break
print('Fim de Jogo')
print('==='*10)