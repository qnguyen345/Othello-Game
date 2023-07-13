import unittest
from Othello import Player, Board, Othello

class TestPlayer(unittest.TestCase):
    def test_get_name(self):
        player = Player("Alice", "black")
        self.assertEqual(player.get_name(), "Alice")

    def test_get_color(self):
        player = Player("Bob", "white")
        self.assertEqual(player.get_color(), "white")


class TestBoard(unittest.TestCase):
    def test_update_board(self):
        board = Board()
        board.update_board("black", 4, 3)
        game_board = board.get_board()
        self.assertEqual(game_board[4][3], "X")

    def test_piece_counts(self):
        board = Board()
        black_counts, white_counts = board.piece_counts()
        self.assertEqual(black_counts, 2)
        self.assertEqual(white_counts, 2)


class TestOthello(unittest.TestCase):
    def test_create_player(self):
        othello = Othello()
        othello.create_player("Alice", "black")
        self.assertEqual(len(othello._players), 1)
        self.assertEqual(othello._players[0].get_name(), "Alice")

    def test_return_available_positions(self):
        othello = Othello()
        othello.create_player("Alice", "black")
        othello.create_player("Bob", "white")
        available_pos = othello.return_available_positions("black")
        self.assertEqual(len(available_pos), 4)

    def test_make_move(self):
        othello = Othello()
        othello.create_player("Alice", "black")
        othello.make_move("black", (4, 3))
        game_board = othello._board.get_board()
        self.assertEqual(game_board[4][3], "X")

    def test_play_game(self):
        othello = Othello()
        othello.create_player("Alice", "black")
        othello.create_player("Bob", "white")
        result = othello.play_game("black", (4, 3))
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()




