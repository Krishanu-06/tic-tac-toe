# print("   |   |   ")
# print("-----------")
# print("   |   |   ")
# print("-----------")
# print("   |   |   ")

def draw_board(positions):
    no_of_cols = 11
    no_of_rows = 5
    for row in range(no_of_rows):
        for col in range(no_of_cols):
            if row % 2 == 0:
                if col == 3 or col == 7:
                    print("|",end="")
                else:
                    if (row == 0 or row == 2 or row == 4) and (col == 1 or col == 5 or col == 9):
                        display_list = (row,col)
                        print(positions[display_list],end="")
                    else:
                        print(" ",end="")
            else:
                print("-",end="")
        print("\n")

# Create a data structure that holds the position 
positions = {    
    (0,1) : 1,
    (0,5) : 2,
    (0,9) : 3,
    (2,1) : 4,
    (2,5) : 5,
    (2,9) : 6,
    (4,1) : 7,
    (4,5) : 8,
    (4,9) : 9
}

mapping_positions = {
    1 : (0,1),
    2 : (0,5),
    3 : (0,9),
    4 : (2,1),
    5 : (2,5),
    6 : (2,9),
    7 : (4,1),
    8 : (4,5),
    9 : (4,9)
}

# Game Variables
is_playing = False
user_status = input("Welcome to tic tac toe press Y if you want to comtinue ")
if(user_status == 'Y' or user_status == 'y'):
    is_playing = True
user = True

while(is_playing):
    if(user == True):
        user_game = "X"
    else:
        user_game = "O" 
    print("\n")
    draw_board(positions)
    print("User ",user_game,"enter the index where you want to input by looking at the board")
    index = int(input())
    if(index < 0 or index > 9):
        print("Enter valid index")
    else:
        change_game_status = mapping_positions[index]
        positions[change_game_status] = user_game
        user = not user 
