#! /usr/bin/python3
# new Tic Tac Toe 2.0!
# 08/07/2020 summer edition!
# by Demian Ruban (yalashara707@gmail.com)

from random import randint

def get_winner(board):
    wins = ((0, 1, 2), (3, 4, 5),
            (6, 7, 8), (0, 3, 6),
            (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6))
    for positions in wins:
        pos_on_board = [board[i] for i in [*positions]]
        if pos_on_board[0] != '_' and len(set(pos_on_board)) == 1:
            return pos_on_board[0]

def get_opponent_for(player):
    return 'X' if player=='O' else 'O'
    
def minimax(board, player, mode) -> int:
    
    if player == get_winner(board):
        return 1

    if mode == 3:
        move = -1
        score = -2
        
        for i in range(9):
            if board[i] == '_':
                board_with_new_move = board
                board_with_new_move[i] = player
                score_for_the_move = -minimax(board_with_new_move,
                                              get_oponnent_for(player))
                if score_for_the_move > score:
                    score = score_for_the_move
                    move = i
    
        if move == -1:
            return 0

        return score


def move(board, player):
    
    moves = {'i': 0, 'o': 1, 'p': 2,
             'k': 3, 'l': 4, ';': 5,
             ',': 6, '.': 7, '/': 8}

    while True:
        user_input = input(player + " make move!: ").lower()

        if 'q' in user_input:
            exit()
        elif user_input in moves and board[moves[user_input]] == '_':
            print() # make line
            board[moves[user_input]] = player
            break
        else:
            print("Wrong input. Try again.")
            continue
    return


def draw_board(board):
    indexes = [0, 1, 2]
    for i in range(3):
        print(' ' + ' | '.join(board[j] for j in indexes))
        if i < 2: print('---+---+---')
        indexes = [j + 3 for j in indexes]
    print()

def ask_mode():
    while True:        
        a = input("Choose game mode:\n"
                  + "1. Play online.\n"
                  + "2. Play at single computer.\n"
                  + "3. Single player.\n\n")
        if a in ('1', '2'):
            return int(a)
        else:
            print("Wrong input. Try again.")
            continue

# Script

board = ['_' for i in range(9)]

player = 'X' if randint(0, 1) == 0 else 'O'

mode = ask_mode()

if mode == 1:
    pass

elif mode == 2:
    while True:
        draw_board(board)
        result = minimax(board, player, mode)
        if result == 1:
            input(player + " won!")
            break
        elif result == 0:
            input("Draw.")
            break
        player = get_opponent_for(player)
        move(board, player)

elif mode == 3:
    computer = get_opponent_for(player)
    while True:
        draw_board(board)
        move(board, player)
