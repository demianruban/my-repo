#! /usr/bin/python3
# new Tic Tac Toe 2.0!
# 08/07/2020 summer edition!
# by Demian Ruban (yalashara707@gmail.com)

# There will no position writing needed anymore
# Moves are made with special keys on keyboard.

def get_winner(board):
    wins = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for index1, index2, index3 in wins:
        pos = [board[index1], board[index2], board[index3]]
        pos[0] if all(e == pos[0] for e in pos) else False

def get_opponent_for(player):
    return 'X' if player=='O' else 'O'
    
def minimax(board, player) -> int:
    return  bool(get_winner(board))
        
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
            board[moves[user_input]] = player
            break
        else:
            print("Wrong input. Try again.")
            continue
    return

def start():
    while True:        
        a = input("Choose game mode:\n"
                  + "1. Two players.\n"
                  + "2. Single player.\n\n")
        if a in ('1', '2'):
            return int(a)
        else:
            print("Wrong input. Try again.")
            continue


def draw_board():
    indexes = [0, 1, 2]
    for i in range(3):
        print(' ' + ' | '.join(board[j] for j in indexes))
        if i < 2: print('---+---+---')
        indexes = [j + 3 for j in indexes]
    print()


def main():
    board = ['_' for i in range(9)]
    player1, player2, computer = '', '', ''
    mode = 0

    while True:
        mode = start()
        if mode == 1:
            player1, player2 = 'X', 'O'
        else:
            computer, player1 = 'X', 'O'
        draw_board()
        move(board, player)

        print(get_winner(board))

if __name__ == '__main__':
    main()

        
