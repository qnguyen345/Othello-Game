# Author: Quyen Nguyen
# Date: 6/5/23
# GitHub Username: qnguyen345
# Description: Othello game on an 8x8 board, excluding the boundaries. It is playable with two players.
# The following code has classes Player, Board, and Othello, where all data members are private.

class Player:
    """A class to represent the players and their piece color.
    This class holds information about the player’s name and their piece color.
    All data members are private.
    Used in Othello class."""

    def __init__(self, name, color):
        """Initializes player's name and color."""
        self._name = name
        self._color = color

    def get_name(self):
        """Gets the player's name."""
        return self._name

    def get_color(self):
        """Gets the player's color."""
        return self._color


class Board:
    """A class to represent the Othello board.
    Stores the condition of the current board and updates it when a move is made.
    All data members are private.
    Used in Othello class."""

    # 10 x 10 board, INCLUDING the boarders
    # star (*) - board's boarder
    # dot (.) - empty space
    # X - black piece
    # O - white piece
    game_board = [
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
        ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
        ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
        ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
        ['*', '.', '.', '.', 'X', 'O', '.', '.', '.', '*'],
        ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
        ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
        ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]

    def __init__(self):
        """Initializes the game board."""
        self._game_board = [row[:] for row in self.game_board]

    def get_board(self):
        """Gets game board."""
        return self._game_board

    def update_board(self, color, row, column):
        """Updates the board at row [row], column [column] with the player's color.
        If the move is valid, it also flips the opponent's pieces according to Othello rules."""

        if color == "black":
            play_color = "X"
            opponent_color = "O"
        elif color == "white":
            play_color = "O"
            opponent_color = "X"
        board = self._game_board
        board[row][column] = play_color

        # Checks adjacent positions if they need to be flipped based on the Othello rules
        adjacent_pos = [-1, 0, 1]
        for row_change in adjacent_pos:
            for col_change in adjacent_pos:
                adjacent_row = row + row_change
                adjacent_col = column + col_change
                positions_to_flip = []      # List of positions to flip

                # Checks if the adjacent positions is within the boundaries and has the opponent's color
                while (1 <= adjacent_row <= 8 and 1 <= adjacent_col <= 8 and
                        board[adjacent_row][adjacent_col] == opponent_color):
                    positions_to_flip.append((adjacent_row, adjacent_col))
                    adjacent_row += row_change
                    adjacent_col += col_change
                    if (1 <= adjacent_row <= 8 and 1 <= adjacent_col <= 8 and
                            board[adjacent_row][adjacent_col] == play_color):

                        # Flips opponent's pieces to playing color piece
                        for flip_row, flip_col in positions_to_flip:
                            board[flip_row][flip_col] = play_color
                        break

    def piece_counts(self):
        """Counts the number of black and white pieces."""
        black_counts = 0
        white_counts = 0

        for row in range(1, 9):
            for col in range(1, 9):
                if self._game_board[row][col] == "X":
                    black_counts += 1
                if self._game_board[row][col] == "O":
                    white_counts += 1

        return black_counts, white_counts


class Othello:
    """Othello class to represent the Othello game.
    Uses Player Class to keep track of the player's color.
    Also uses Board Class to update and keep track of the piece’s position in the board.
    All data members are private."""

    def __init__(self):
        """Initializes the board and the list of players."""
        self._board = Board()
        self._players = []

    def create_player(self, player_name, color):
        """Adds the player's name and color to the player list."""
        player_info = Player(player_name, color)
        self._players.append(player_info)

    def print_board(self):
        """Prints out the current board."""
        board = self._board.get_board()

        # Prints each row and column in the board with double spaces between the values
        for row in range(0, 10):
            for col in range(0, 10):
                print(board[row][col], end = "  ")
            print()

    def return_available_positions(self, color):
        """Returns a list of available positions for the specified color."""
        available_pos = []
        player_pos = []
        opponent_pos = []
        board = self._board.get_board()

        if color == "black":
            play_color = "X"
            opponent_color = "O"
        elif color == "white":
            play_color = "O"
            opponent_color = "X"

        # Finds the player's and opponent's positions on the board
        for row in range(1, 9):
            for col in range(1, 9):
                if board[row][col] == play_color:
                    player_pos.append((row, col))
                elif board[row][col] == opponent_color:
                    opponent_pos.append((row, col))

        # Checks the adjacent positions
        adjacent_pos = [-1, 0, 1]
        for row, col in player_pos:
            for row_change in adjacent_pos:
                for col_change in adjacent_pos:
                    adjacent_row = row + row_change
                    adjacent_col = col + col_change

                    # Check if adjacent positions are within boundaries and have opponent's color
                    while (1 <= adjacent_row <= 9 and 1 <= adjacent_col <= 9 and
                           board[adjacent_row][adjacent_col] == opponent_color):
                        adjacent_row += row_change
                        adjacent_col += col_change

                        # Checks if adjacent positions are within boundaries and is empty
                        if (1 <= adjacent_row <= 9 and 1 <= adjacent_col <= 9 and
                                board[adjacent_row][adjacent_col] == "."):

                            # Adds the adjacent positions to available positions
                            if (adjacent_row, adjacent_col) not in available_pos:
                                available_pos.append((adjacent_row, adjacent_col))
                            break

        # Sorts list to pass GradeScope grading
        available_pos.sort()
        return available_pos

    def make_move(self, color, piece_position):
        """ Handles the player’s move in the game.
        It puts the piece at the specified position on the board and updates it.
        Returns a printout of the updated board."""

        row, col = piece_position
        self._board.update_board(color, row, col)
        board = self._board.get_board()  # Gets the updated board
        return board

    def play_game(self, player_color, piece_position):
        """ Allows the player to make a move and check if the move is valid.
        It updates the game/board based on the conditions under Returns.
        Returns: A print statement and a list (of positions).
                The statement and list can be one of the following based on the condition of the moves:
                    If the move to a position is valid
                        - Makes the move
                        - Updates the board by calling update_board
                    If the move to a position is invalid
                        - 'Invalid move'
                        - 'Here are the valid moves:' (list of possible positions)
                    If no valid move/positions exists
                        - 'No valid move exists.'
                        - returns empty list
                    If the game ended
                        'The game has ended:
                        (number of) black piece
                        (number of) white piece.' """

        row, col = piece_position

        if player_color == "black":
            opponent_color = "white"
        elif player_color == "white":
            opponent_color = "black"

        # Available positions for playing pieces
        available_pos = self.return_available_positions(player_color)
        # Available positions for opponent's pieces
        opponent_available_pos = self.return_available_positions(opponent_color)

        # Move list is empty
        if not available_pos:
            print("No valid moves.")

        # Move list of both players are empty
        elif not available_pos and opponent_available_pos:
            black_counts, white_counts = self._board.piece_counts()
            print("The game has ended: ", black_counts, " black pieces", white_counts, " white pieces.")
            self.return_winner()

        # The desired move is valid (exists in the move list)
        elif (row, col) in available_pos:
            self.make_move(player_color, piece_position)

        # There are positions in the list but the desired move is not in the list
        elif (row, col) not in available_pos:
            print("Here are the valid moves:", available_pos)
            return "Invalid move"


    def return_winner(self):
        """Prints the winner and their counts when the game is finished."""

        black_counts, white_counts = self._board.piece_counts()
        black_winner = None
        white_winner = None

        # Gets winner name
        for player in self._players:
            if player.get_color() == "black":
                black_winner = player.get_name()
            elif player.get_color() == "white":
                white_winner = player.get_name()

        # Compares the counts of pieces on the board to find the winner
        if black_counts < white_counts:
            print("Winner is white player:", white_winner)
        elif black_counts > white_counts:
            print("Winner is black player:", black_winner)
        elif black_counts == white_counts:
            print("It's a tie.")