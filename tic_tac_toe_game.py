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

# Check if game is over
def check_win(is_playing):
    # Diagonal check
    d1 = positions[mapping_positions[1]]
    d2 = positions[mapping_positions[5]]
    d3 = positions[mapping_positions[9]]
    d4 = positions[mapping_positions[3]]
    d5 = positions[mapping_positions[5]]
    d6 = positions[mapping_positions[7]]
    if d1 == d2 and d1 == d3:
        is_playing = False
        return is_playing
    if d4 == d5 and d4 == d6:
        is_playing = False
        return is_playing

    no_status = False
    for i in range(9):
        index = i + 1
        if(index == 1 or index == 4 or index == 7) and (positions[mapping_positions[index]] == positions[mapping_positions[index + 1]]) and (positions[mapping_positions[index]] == positions[mapping_positions[index + 2]]):
            is_playing = False
            return is_playing
        if (index == 1 or index == 2 or index == 3) and (positions[mapping_positions[index]] == positions[mapping_positions[index + 3]]) and (positions[mapping_positions[index]] == positions[mapping_positions[index + 6]]):
            is_playing = False
            return is_playing
        if(positions[mapping_positions[index]] != "X" or positions[mapping_positions[index]] != "O"):
            no_status = True

    if(no_status == False):
        is_playing = False
    return is_playing

# Check if input address is valid
def is_valid_position(index):
    is_valid = True
    if index <= 0 or index > 9:
        is_valid = False
        return is_valid
    for i in  positions:
        if positions[i] == index:
            is_valid = False
            return is_valid
    return is_valid


def maintain_game(user):
    if(user == True):
        user_game = "X"
    else:
        user_game = "O"
    print("\n")
    draw_board(positions)
    print("User ",user_game," enter the index where you want to input by looking at the board")
    index = int(input())
    is_valid = is_valid_position(index)
    if(is_valid):
        print("Enter valid index")
    else:
        change_game_status = mapping_positions[index]
        positions[change_game_status] = user_game
        user = not user
    return user

# Game loop
while(is_playing):
    if(check_win(is_playing)):
        user = maintain_game(user)
    else:
        draw_board(positions)
        print("Game Over \n")
        break
