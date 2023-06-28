from oNx import oNx

def char_player(player):
    if player == 1:
        return "O"
    else:
        return "X"

def play_game():
    game = oNx()
    player = 1
    welcome_list = [
        "                                                Welcome to ",
        "        _______             ________ ",            
        "  ____  \      \ ___  ___  /  _____/_____    _____   ____ ",
        " /  _ \ /   |   \\  \/  / /   \  ___\__  \  /     \_/ __ \ ",
        "(  <_> )    |    \>    <  \    \_\  \/ __ \|  Y Y  \  ___/ ",
        " \____/\____|____/__/\__\  \________(______/__|_|__/\____| ",
        "",
        "Intense 1v1, winner takes all action! ",
    ]

    welcome_string = '\n'.join(welcome_list)
    print(welcome_string)

    while True:
        print("\n")
        print(game)
        print(f"Player {char_player(game.get_player)}'s turn:")
        row = int(input("Enter the row number (0, 1, or 2): "))
        col = int(input("Enter the column number (0, 1, or 2): "))

        try:
            game_state = game.make_move(row, col)
        except ValueError as e:
            print(f"Invalid move")
            continue
        
        if game_state in [1, 2]:
            print(game)
            print(f"{char_player(player)} wins!")
            break
        elif game_state == 3:
            print(game)
            print("It's a draw!")
            break

def main():
    play_game()


if __name__ == "__main__":
    main()