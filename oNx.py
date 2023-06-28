import numpy as np


class oNx:
    """
    oNx game class.

    Represents a game of oNx, a variant of tic-tac-toe played on a 3x3 grid.
    The game supports two players who take turns making moves on the board.
    The goal is to be the first player to form a horizontal, vertical, or diagonal line of three of their own symbols.

    Attributes:
        __board (numpy.ndarray): The game board represented as a 3x3 Numpy array.
        __current_player (numpy.int8): The current player number (1 or 2).

    Methods:
        __init__: Initializes a new instance of the oNx class.
        __start_game: Start the game and initialize any necessary state or variables.
        make_move: Make a move on the game board for the specified player at the given row and column.
        __is_valid_move: Check if a move at the specified row and column is valid.
        __update_player: Update the current player.
        __check_win: Check if the specified player has won.
        __check_draw: Check if the game has ended in a draw.
        __game_state: Get the current state of the game.
        reset_game: Reset the game state, including the game board, for a new round.
        get_board: Get the current game board.
        __str__: Returns a nicely formatted ASCII representation of the game board.
    """

    def __init__(self):
        """
        Constructor for the oNx class.
        It sets up a new game state by invoking the '__start_game' method.
        """
        self.__board = np.zeros((3, 3), dtype=np.int8)
        self.__current_player = np.int8(1)
        self.__move = np.int8([0, 0])

    def get_player(self):
        """
        Get the current player number.

        Returns:
            int: The current player number (1 or 2).
        """
        return self.__current_player

    def make_move(self, row, col):
        """
        Make a move on the game board for the specified player at the given row
        and column.
        Update the game state and check for win or draw conditions.

        Args:
            player (int): The player number (1 or 2).
            row (int): The row index of the move (0, 1, or 2).
            col (int): The column index of the move (0, 1, or 2).

        Returns:
            int: The current game state:
                - 0: Ongoing
                - 1: Player 1 wins
                - 2: Player 2 wins
                - 3: Draw
        """
        self.__move = [row, col]
        self.__is_valid_move()
        self.__board[self.__move[0], self.__move[1]] = self.__current_player
        game_state = self.__game_state()
        self.__update_player()
        return game_state

    def __is_valid_move(self):
        """
        Check if a move at the specified row and column is valid (i.e., within
        bounds and the cell is empty).
        Raise a ValueError if the move is invalid.
        """
        for i in self.__move:
            if not isinstance(i, int):
                raise TypeError("Row and column must be integers")
        if (
            self.__move[0] < 0
            or self.__move[0] > 2
            or self.__move[1] < 0
            or self.__move[1] > 2
        ):
            raise ValueError("Invalid row or column")
        if self.__board[self.__move[0], self.__move[1]] != 0:
            raise ValueError("Cell is already occupied")

    def __update_player(self):
        """
        Update the current player.
        """
        self.__current_player = np.int8(3) ^ self.__current_player

    def __check_win(self, player):
        """
        Check if the specified player has won.

        Args:
            player (int): The player number (1 or 2).

        Returns:
            bool: True if the player has won, False otherwise.
        """
        for i in np.int8([0, 1, 2]):
            if (
                self.__board[i, 0] == self.__board[i, 1] == self.__board[i, 2] == player
                or self.__board[0, i]
                == self.__board[1, i]
                == self.__board[2, i]
                == player
            ):
                return True

        if (
            self.__board[0, 0] == self.__board[1, 1] == self.__board[2, 2] == player
            or self.__board[0, 2] == self.__board[1, 1] == self.__board[2, 0] == player
        ):
            return True

        return False

    def __check_draw(self):
        """
        Check if the game has ended in a draw (i.e., all cells on the board are
        filled).

        Returns:
            bool: True if it's a draw, False otherwise.
        """
        return np.all(self.__board != 0)

    def __game_state(self):
        """
        Get the current state of the game.

        Returns:
            int: The current game state:
                - 0: Ongoing
                - 1: Player 1 wins
                - 2: Player 2 wins
                - 3: Draw
        """
        if self.__check_win(self.__current_player):
            return self.__current_player

        elif self.__check_draw():
            return 3

        else:
            return 0

    def reset_game(self):
        """
        Reset the game state, including the game board, for a new round.
        """
        self.__board = np.zeros((3, 3), dtype=np.int8)
        self.__current_player = np.int8(1)

    def get_board(self):
        """
        Get the current game board.

        Returns:
            numpy.ndarray: The current game board.
        """
        return self.__board

    def __str__(self):
        """
        Returns a nicely formatted ASCII representation of the game board.
        """
        symbols = {0: " ", 1: "X", 2: "O"}
        board_str = ""
        for row in range(3):
            for col in range(3):
                symbol = symbols[self.__board[row, col]]
                board_str += f" {symbol} "
                if col < 2:
                    board_str += "|"
            if row < 2:
                board_str += "\n---+---+---\n"
        return board_str


def main():
    # Your main code logic here
    pass


if __name__ == "__main__":
    main()
