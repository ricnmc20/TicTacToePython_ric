# write your code here
empty_cells = 1
moves = []


def matrix_initiate():
    global moves
    moves = [["_" for i in range(3)] for j in range(3)]


def print_field(field):
    print("---------")
    print("|", " ".join(field[0]), "|")
    print("|", " ".join(field[1]), "|")
    print("|", " ".join(field[2]), "|")
    print("---------")


def play_move():
    global empty_cells
    wins = True
    draw = True
    count = 0
    gamer = "X"
    while wins and draw:
        print(f"Enter the coordinates for: {gamer}")
        try:
            user_input = input().split()
            if len(user_input) != 2:
                print("You must enter exactly two numbers separated by a space!")
                continue  # restart the loop
            x, y = map(int, user_input)
            if x > 3 or y > 3:
                print("Coordinates should be from 1 to 3!")
                continue
            elif x < 1 or y < 1:
                print("Coordinates should be from 1 to 3!")
                continue
            elif moves[x - 1][y - 1] != "_":
                print("This cell is occupied! Choose another one!")
                continue  # restart the loop

            if count == 0:
                gamer = "O"
                moves[x - 1][y - 1] = "X"
            elif count % 2 == 0:
                gamer = "O"
                moves[x - 1][y - 1] = "X"
                validate_plays(moves)
            else:
                gamer = "X"
                moves[x - 1][y - 1] = "O"
                validate_plays(moves)
            print_field(moves)
            count += 1
            empty_cells += 1

        except ValueError:
            print("You should enter numbers!")


def check_two_wins(win_):
    if win_ >= 2:
        print("Impossible")
        exit(0)


def check_repeat(x, y):
    global empty_cells

    for i in range(3):
        for j in range(3):
            if moves[i][j] == "X":
                x += 1
            elif moves[i][j] == "O":
                y += 1
            elif moves[i][j] == "_":
                empty_cells += 1
    if abs(x - y) >= 2:
        print("Impossible")


def validate_plays(moves_):
    win = 0
    win_play = ""
    # Check the rows
    for i in range(3):
        if moves_[i][0] == moves_[i][1] == moves_[i][2] != "_":

            win += 1
            check_two_wins(win)
            win_play = f"{moves_[i][0]} wins"

    # Check the columns
    for i in range(3):
        if moves_[0][i] == moves_[1][i] == moves_[2][i] != "_":

            win += 1
            check_two_wins(win)
            win_play = f"{moves_[0][i]} wins"

    # Check the diagonals
    if moves_[0][0] == moves_[1][1] == moves_[2][2] != "_":

        win += 1
        check_two_wins(win)
        win_play = f"wins {moves_[1][1]}"
    if moves_[0][2] == moves_[1][1] == moves_[2][0] != "_":

        win += 1
        check_two_wins(win)
        win_play = f"{moves_[1][1]} wins"

    if win == 0 and empty_cells == 9:
        print_field(moves)
        print("Draw")
        print('Good luck!')
        exit(0)

    elif win == 1:
        print_field(moves)
        print(win_play)
        print('Good luck!')
        exit(0)


matrix_initiate()
print_field(moves)
play_move()
