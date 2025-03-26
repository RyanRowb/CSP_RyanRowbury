#Ryan R (The cool one) Win detector!

#grid
grid = [[1,2,3],
[4,5,6],
[7,8,9]]

for grid in grid:
    print(f" {grid[0]} | {grid[1]} | {grid[2]}\n --+---+--")

#Johann, Hines
grid = [["1","2","3"], "\n",
["4","5","6"], "\n",
["7","8","9"], "\n"]

game_finished = False 
taken = []
while game_finished == False:
        spot = input("pick a number for your spot 1-9\n !!!SPELL OUT DONT TYPE A NUMBER!!!\n").strip().upper()
    
        if spot in taken:
            print("That spot is taken.")
        else: 
            taken.append(spot)
            if spot == "ONE":
                grid[0][0]="X"
            elif spot == "TWO":
                grid[0][1]  ="X"
            elif spot == "THREE":
                grid[0][2] ="X"
            elif spot == "FOUR":
                grid[1][0]="X"
            elif spot == "FIVE": 
                grid[1][1]="X"
            elif spot == "SIX":
                grid[1][2] ="X"
            elif spot == "SEVEN":
                grid[2][0] ="X"
            elif spot == "EIGHT":
                grid[2][1] ="X"
            elif spot == "NINE":
                grid[2][2] ="X"
            break


print(grid)
    
print(taken)

#Ryan R (The cool one) Win detector!
   
def win(grid):
        if  grid[0][0] == "X" and grid[0][1] =="X" and grid[0][2] =="X":
            print("X wins")
            set (game_finsished = True)
        elif grid[1][0] == "X" and grid[1][1] =="X" and grid[1][2] =="X":
            print("X wins")
            set (game_finsished = True)
        elif grid[2][0] == "X" and grid[2][1] =="X" and grid[2][2] =="X":
            print("X wins")
            set (game_finsished = True)
        elif grid[0][0] == "O" and grid[0][1] =="O" and grid[0][2] =="O":
            print("O wins")
            set (game_finsished = True)
        elif grid[1][0] == "O" and grid[1][1] =="O" and grid[1][2] =="O":
            print("O wins")
            set (game_finsished = True)
        elif grid[2][0] == "O" and grid[2][1] =="O" and grid[2][2] =="O":
            print("O wins")
            set (game_finsished = True)
        elif grid[0][0] == "X" and grid[1][0] =="X" and grid[2][0] =="X":
            print("X wins")
            set (game_finsished = True)
        elif grid[0][1] == "X" and grid[1][2] =="X" and grid[2][2] =="X":
            print("X wins")
            set (game_finsished = True)
        elif grid[0][2] == "X" and grid[1][2] =="X" and grid[2][2] =="X":
            print("X wins")
            set (game_finsished = True)
        elif grid[0][0] == "X" and grid[1][1] =="X" and grid[2][2] =="X":
            print("X wins")
            set (game_finsished = True)
        elif grid[0][2] == "X" and grid[1][1] =="X" and grid[2][0] =="X":
            print("X wins")
            set (game_finsished = True)
        elif grid[0][0] == "O" and grid[1][0]=="O" and grid[2][0]=="O":
            print("O wins")
            set (game_finsished = True)
        elif grid[0][1] == "O" and grid[1][2]=="O" and grid[2][2]=="O":
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

win(grid)

print(grid)