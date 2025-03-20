#Ryan R (The cool one) Win detector!

#grid
grid = [[1,2,3],
[4,5,6],
[7,8,9]]

for grid in grid:
    print(f" {grid[0]} | {grid[1]} | {grid[2]}\n --+---+--")

grid = [["X",2,3],
["X",5,6],
["X",8,9]]
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
    elif grid[0][1][2]==["X"]:
        print("X wins")
win(grid)