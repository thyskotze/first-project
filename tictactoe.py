# | | 0
# -----1
# | | 2
# -----3
# | | 5
# 01234

# definitions

def drawField(field):
    for row in range(5):
        if row % 2 == 0:
            practicalRow = int(row / 2)
            # this will be the writing line
            for col in range(5):
                if col % 2 == 0:
                    practicalColumn = int(col / 2)
                    if col != 4:
                        print(field[practicalColumn][practicalRow], end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|", end="")
            else:
                print("-" * 5)


# ----------------------------------------------------------------------------------------------
# variables
player = 1
currentField = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
# this will be the list that stores the current layout of the field, elemants are columns
# element1 = column1 so this element 1 will contain 3 values and the best way to do it is with a nested list
# element2 = column2
# element3 = column3
# currentField = currentField = [  ["A1","A2","A3"],
#                                 ["B1","B2","B3"],
#                                 ["C1","C2","C3"]]
# -----------------------------------------------------------------------------------------------
drawField(currentField)
while (True):  # This is a infanate loop =, the same thing can be done with a for loop that itterates 9 times
    print("Player ", player)
    MoveCol = int(input("Please enter the column number: \n"))  # this asks for user input, the user needs to provide the column number
    MoveRow = int(input("Please enter the row number: \n"))  # this askes for the row number that the user would like to use
    if player == 1:  # Here we are making it players 1's turn
        if currentField[MoveCol][MoveRow] == " ":  # this statment checks if the location of the col and row entered by the player is available or empty
            currentField[MoveCol][MoveRow] = "X"  # if it is empty we assign a 'X' to the location
            player = 2  # this assignes the value of 2 to the variable named player, so that it will become his/here turn next
    else:
        if currentField[MoveCol][MoveRow] == " ":  # here we check the value of the locaton for the second player
            currentField[MoveCol][MoveRow] = "O"
            player = 1
    drawField(currentField)

#this thing needs completion = Like the lazy teacher said its a bunch of if statment. I will learn more and come back