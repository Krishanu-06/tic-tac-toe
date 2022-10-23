# print("   |   |   ")
# print("-----------")
# print("   |   |   ")
# print("-----------")
# print("   |   |   ")

def draw_board():
    no_of_cols = 11
    no_of_rows = 5
    for row in range(no_of_rows):
        for col in range(no_of_cols):
            if row % 2 == 0:
                if col == 3 or col == 7:
                    print("|",end="")
                else:
                    print(" ",end="")
            else:
                print("-",end="")
        print("\n")

draw_board()