def win(grid):
        if  grid[0][0] == "X" and grid[0][1]=="X" and grid[0][2]=="X":
            print("X wins")
            set (game_finsished = True)
        elif grid[1]==["X", "X", "X"]:
            print("X wins")
            set (game_finsished = True)
        elif grid[2]==["X", "X", "X"]:
            print("X wins")
            set (game_finsished = True)
        elif grid[0]==["O", "O", "O"]:
            print("O wins")
            set (game_finsished = True)
        elif grid[1]==["O", "O", "O"]:
            print("O wins")
            set (game_finsished = True)
        elif grid[2]==["O", "O", "O"]:
            print("O wins")
            set (game_finsished = True)
        elif grid[0][0] == "X" and grid[1][0]=="X" and grid[2][0]=="X":
            print("X wins")
            set (game_finsished = True)
        elif grid[0][1] == "X" and grid[1][2]=="X" and grid[2][3]=="X":
            print("X wins")
            set (game_finsished = True)
        elif grid[0][2] == "X" and grid[1][2]=="X" and grid[2][2]=="X":
            print("X wins")
            set (game_finsished = True)
        elif grid[0][0] == "X" and grid[1][1]=="X" and grid[2][2]=="X":
            print("X wins")
            set (game_finsished = True)
        elif grid[0][2] == "X" and grid[1][1]=="X" and grid[2][0]=="X":
            print("X wins")
            set (game_finsished = True)
        elif grid[0][0] == "O" and grid[1][0]=="O" and grid[2][0]=="O":
            print("O wins")
            set (game_finsished = True)
        elif grid[0][1] == "O" and grid[1][2]=="O" and grid[2][3]=="O":
            print("O wins")
            set (game_finsished = True)
        elif grid[0][2] == "O" and grid[1][2]=="O" and grid[2][2]=="O":
            print("O wins")
            set (game_finsished = True)
        elif grid[0][0] == "O" and grid[1][1]=="O" and grid[2][2]=="O":
            print("O wins")
            set (game_finsished = True)
        elif grid[0][2] == "O" and grid[1][1]=="O" and grid[2][0]=="O":
            print("O wins")
            set (game_finsished = True)
        elif grid[0][0] == ("X" or "O") and grid[0][1] == ("X" or "O") and grid[0][2] == ("X" or "O") and grid[1][0] == ("X" or "O") and grid[1][1] == ("X" or "O") and grid[1][2] == ("X" or "O") and grid[2][0] == ("X" or "O") and grid[2][1] == ("X" or "O") and grid[2][2] == ("X" or "O"):
             print("Its a tie.")
             set (game_finsished = True)
        else:
            print("Yo.")