def win(grid):

    if   grid[0][0] == "X" and grid[0][1]=="X" and grid[0][2]=="X":
         print("X wins")
         set(game_finished = True)
    elif grid[1][0] == "X" and grid[1][1]=="X" and grid[1][2]=="X":
        print("X wins")
        set(game_finished = True)
    elif grid[2][0] == "X" and grid[2][1]=="X" and grid[2][2]=="X":
        print("X wins")
        set(game_finished = True)
    elif grid[0][0] == "O" and grid[0][1]=="O" and grid[0][2]=="O":
        print("O wins")
        set(game_finished = True)
    elif grid[1][0] == "O" and grid[1][1]=="O" and grid[1][2]=="O":
        print("O wins")
        set(game_finished = True)
    elif grid[2][0] == "O" and grid[2][1]=="O" and grid[2][2]=="O":
        print("O wins")
        set(game_finished = True)
    elif grid[0][0] == "X" and grid[1][0]=="X" and grid[2][0]=="X":
        print("X wins")
        set(game_finished = True)
    elif grid[0][0] == "X" and grid[1][1]=="X" and grid[2][2]=="X":
        print("X wins")
        set(game_finished = True)
    elif grid[0][2] == "X" and grid[1][2]=="X" and grid[2][2]=="X":
        print("X wins")
        set(game_finished = True)
    elif grid[0][0] == "X" and grid[1][1]=="X" and grid[2][2]=="X":
        print("X wins")
        set(game_finished = True)
    elif grid[0][2] == "X" and grid[1][1]=="X" and grid[2][0]=="X":
        print("X wins")
        set(game_finished = True)
    elif grid[0][1] == "X" and grid[1][1]=="X" and grid[2][1]=="X":
        print("X wins")
        set(game_finished = True)
    elif grid[0][0] == "O" and grid[1][0]=="O" and grid[2][0]=="O":
        print("O wins")
        set(game_finished = True)
    elif grid[0][0] == "O" and grid[1][1]=="O" and grid[2][2]=="O":
        print("O wins")
        set(game_finished = True)
    elif grid[0][2] == "O" and grid[1][2]=="O" and grid[2][2]=="O":
        print("O wins")
        set(game_finished = True)
    elif grid[0][0] == "O" and grid[1][1]=="O" and grid[2][2]=="O":
        print("O wins")
        set(game_finished = True)
    elif grid[0][2] == "O" and grid[1][1]=="O" and grid[2][0]=="O":
        print("O wins")
        set(game_finished = True)
    elif grid[0][1] == "O" and grid[1][1]=="O" and grid[2][1]=="O":
        print("O wins")
        set(game_finished = True)
    elif all(spot in ["X", "O"] for row in grid for spot in row):
        print("It's a tie.")
        set(game_finished = True)
    return grid