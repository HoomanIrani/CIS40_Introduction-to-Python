#CIS40_Chapter 6 Assignment P6.28_ Houman Irani
#write a program to creat a tic-tac-toc play game!


game = [[0,0,0],
        [0,0,0],
        [0,0,0],]

    
#main function show whole processes in order
def main():
    flag = True
    while flag:
        display_table()
        player,row,column = get_input()
        game_process(player,row,column)
        flag = winner_check()

#set a set to diaplay a paly table
def display_table():
    print("Tic_Tac_toc play table")
    print("   0  1  2")
    count = 0
    for row in game:
        print(count,row)
        count += 1
    print("play rules:\n\"1\"instead of player1,and \"-1\" instead of players2\n\
type row index number and column index number to choose which block set your symble")


#get information from user    
def get_input():
    player = input("Player 1 or player 2(enter 1/2):")
    row = int(input("Row number:"))
    column = int(input("Column number:"))
    return player,row,column

#change the position by player's indecation
def game_process(player,row,column):
    if player == "1":
        game[row][column] = 1
    elif player == "2":
        game[row][column] = -1
    return game

#report "winner" when the conditions is valid 
def winner_check():
    for row in game:
        if row[0] == row[1] and row[0] == row[2] and row[0] != 0:
            if row[0] == 1:
                print("Victory!,player1")
                return False
        if row[0] == -1:
                print("Victory!,player2")
                return False
    colum0 = game[0][0] + game[1][0] + game[2][0]
    colum1 = game[0][1] + game[1][1] + game[2][1]
    colum2 = game[0][2] + game[1][2] + game[2][2]
    diag1 = game[0][0] + game[1][1] + game[2][2]
    diag2 = game[0][2] + game[1][1] + game[2][0]
    if colum0 == 3 or colum1 == 3 or colum2 == 3 or diag1 == 3 or diag2 == 3 :
        print("Victory!Player1")
        return False
    elif colum0 == -3 or colum1 == -3 or colum2 == -3 or diag1 == -3 or diag2 == -3:
        print("Victory!Player2")
        return False
    return True

main()

'''

Output1:
Tic_Tac_toc play table
   0  1  2
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 0, 0]
play rules:
"1"instead of player1,and "-1" instead of players2
type row index number and column index number to choose which block set your symble
Player 1 or player 2(enter 1/2):1
Row number:0
Column number:0
Tic_Tac_toc play table
   0  1  2
0 [1, 0, 0]
1 [0, 0, 0]
2 [0, 0, 0]
play rules:
"1"instead of player1,and "-1" instead of players2
type row index number and column index number to choose which block set your symble
Player 1 or player 2(enter 1/2):1
Row number:0
Column number:1
Tic_Tac_toc play table
   0  1  2
0 [1, 1, 0]
1 [0, 0, 0]
2 [0, 0, 0]
play rules:
"1"instead of player1,and "-1" instead of players2
type row index number and column index number to choose which block set your symble
Player 1 or player 2(enter 1/2):1
Row number:0
Column number:2
Victory!,player1


Output2:
Tic_Tac_toc play table
   0  1  2
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 0, 0]
play rules:
"1"instead of player1,and "-1" instead of players2
type row index number and column index number to choose which block set your symble
Player 1 or player 2(enter 1/2):1
Row number:0
Column number:0
Tic_Tac_toc play table
   0  1  2
0 [1, 0, 0]
1 [0, 0, 0]
2 [0, 0, 0]
play rules:
"1"instead of player1,and "-1" instead of players2
type row index number and column index number to choose which block set your symble
Player 1 or player 2(enter 1/2):1
Row number:1
Column number:1
Tic_Tac_toc play table
   0  1  2
0 [1, 0, 0]
1 [0, 1, 0]
2 [0, 0, 0]
play rules:
"1"instead of player1,and "-1" instead of players2
type row index number and column index number to choose which block set your symble
Player 1 or player 2(enter 1/2):1
Row number:2
Column number:2
Victory!Player1
'''


    
