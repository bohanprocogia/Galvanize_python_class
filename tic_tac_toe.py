# This file will play a tic tac toe game

def main():
    tic_tac_toe()

if __name__ == '__main__':
    main()

# functions are need
def tic_tac_toe():
    curr_board = initial_board()   # This will generate a  board
    print_board(curr_board)
    lst_pl1 = []
    lst_pl2 = []
    while win is False:
        player1 = raw_input("Please enter the location for player1 in the format (*,*): ")
        lst_pl1.append(player1)
        curr_board = player(player1,1)
        print_board(curr_board)
        win = win(lst_pl1,player1)

        if win is TRUE:
            print "player 1 wins"
            break
        else:
            player2 = raw_input("Please enter the location for player2 in the format (*,*): ")
            lst_pl2.append(player2)
            curr_board = player(player2,2)
            print_board(curr_board)
            win = win(lst_pl2,player2)
        print "player2 wins"


def initial_board():
    line1 = [(1,1),(1,2),(1,3)]
    line2 = [(2,1),(2,2),(2,3)]
    line3 = [(3,1),(3,2),(3,3)]
    board = [line1,line2,line3]

    return board

def print_board(board):
    for line in board:
        print line


def player(var,flag_player):
    if flag_player == 1:
        curr_board[var[0]][var[1]] == 'X'
    elif flag_plaer == 2:
        curr_board[var[0]][var[1]] == 'O'
    return curr_board

def find(lst,a):
    result = []
    for i, x in enumerate(lst):
        if x==a:
            result.append(i)
    return result

def win(lst,flag_player):
    row = []
    col = []
    if (1,1) in lst and (2,2) in lst and (3,3) in lst:
        print flag_player,"wins"
        return False
    elif (3,1) in lst and (2,2) in lst and (1,3) in lst:
        print flag_player,"wins"
        return False
    else:
        for x in lst:
            row.append(x[0])
            col.append(x[1])
        for i in range(len(row)):
            if row.count(row[i]) == 3 or col.count(col[i]) == 3:
                print flag_player,"wins"
                break
        return False
    return True
