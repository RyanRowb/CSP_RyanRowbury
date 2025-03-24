#Ryan R (The cool one) Win detector!

#grid
grid = [[1,2,3],
[4,5,6],
[7,8,9]]

for grid in grid:
    print(f" {grid[0]} | {grid[1]} | {grid[2]}\n --+---+--")

grid = [["O",2,3],
        ["X","O",6],
        ["X",8,"O"]]

#Ryan R (The cool one) Win detector!
def win(grid):
    if grid[0]==["X","X","X"]:
        print("X wins")
    elif grid[1]==["X", "X", "X"]:
        print("X wins")
    elif grid[2]==["X", "X", "X"]:
        print("X wins")
    elif grid[0]==["O", "O", "O"]:
        print("O wins")
    elif grid[1]==["O", "O", "O"]:
        print("O wins")
    elif grid[2]==["O", "O", "O"]:
        print("O wins")
    elif grid[0][0]=="X" and grid[1][0]=="X" and grid[2][0]=="X":
        print("X wins")
    elif grid[0][1]=="X" and grid[1][2]=="X" and grid[2][3]=="X":
        print("X wins")
    elif grid[0][2]=="X" and grid[1][2]=="X" and grid[2][2]=="X":
        print("X wins")
    elif grid[0][0]=="X" and grid[1][1]=="X" and grid[2][2]=="X":
        print("X wins")
    elif grid[0][2]=="X" and grid[1][1]=="X" and grid[2][0]=="X":
        print("X wins")
    elif grid[0][0]=="O" and grid[1][0]=="O" and grid[2][0]=="O":
        print("O wins")
    elif grid[0][1]=="O" and grid[1][2]=="O" and grid[2][3]=="O":
        print("O wins")
    elif grid[0][2]=="O" and grid[1][2]=="O" and grid[2][2]=="O":
        print("O wins")
    elif grid[0][0]=="O" and grid[1][1]=="O" and grid[2][2]=="O":
        print("O wins")
    elif grid[0][2]=="O" and grid[1][1]=="O" and grid[2][0]=="O":
        print("O wins")
    elif taken.append(spot)
    else:
        print("You tied")
win(grid)