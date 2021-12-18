import random
import os
import sys

def func_quit_game(esc_play):
    esc_play
    if esc_play.strip().upper() == "SAIR":
        print("**** OBRIGADO POR JOGAR ****!")
        sys.exit()
    elif esc_play.strip().upper() == "RESET":
        return (esc_play)

def valid_value(esc_play):
    esc_play
    try:
        esc_play = str(esc_play).upper()
        if esc_play == ('PEDRA') or esc_play == ('PAPEL') or esc_play == ('TESOURA'):
            return esc_play
        elif esc_play == 'RESET':
            return esc_play
    except NameError:
        print('Except TRY {}'.format(esc_play))
        return None


def main_game():
    cont_play = 0
    cont_comp = 0
    cont_emp = 0

    while True:
        print("#"*40)
        print('\n\t\t ***PLACAR ***\nPlayer: {}\nComputer: {}\nEmpate: {}'.format(cont_play, cont_comp, cont_emp))

        comp_esc = random.choice(['PEDRA','PAPEL','TESOURA']).upper()
        print('\nESCOLHA ENTRE PEDRA, PAPEL OU TESOURA:')
        esc_play = input('Escolha PLAY: ').upper()
        func_quit_game(esc_play)
        esc_play = valid_value(esc_play)

        print('PARA SAIR DIGITE [ SAIR ]')
        print('PARA REINICIAR DIGITE [ RESET ]')

        if esc_play is None:
            print("Erro: VOCÊ DEVE DIGITAR UMA DAS OPÇOES: .\n")
            continue
        elif esc_play == 'PEDRA' and  comp_esc == 'TESOURA':
            print('!!! Você Ganhou !!!')
            print('\tPlayer: {} \n\t\tesc \n\tComputador:{}'.format(esc_play, comp_esc))
            cont_play = cont_play+1

        elif esc_play == 'PAPEL' and comp_esc == 'PEDRA':
            print('!!! Você Ganhou !!!')
            cont_play = cont_play + 1
            continue

        elif esc_play == 'TESOURA' and comp_esc =='PAPEL':
            print('!!! Você Ganhou !!!')
            cont_play = cont_play + 1
            continue

        elif esc_play == comp_esc:
            print('!!!!Vocês Empatarem!!!')
            cont_emp = cont_emp + 1
            continue

        elif esc_play == 'RESET':
            print('######  GAME REINICIADO  ######')
            cont_play = 0
            cont_comp = 0
            cont_emp = 0
            continue
        else:
            print('Você Perdeu:')
            cont_comp = cont_comp + 1

main_game()
