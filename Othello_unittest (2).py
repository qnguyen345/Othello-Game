from Othello import Othello

game = Othello()
game.create_player("Helen", "white")
game.create_player("Leo", "black")
game.print_board()
game.play_game("black", (5,6))
game.print_board()
game.play_game("white", (7,6))
game.print_board()
game.play_game("white", (6,6))
game.print_board()
game.play_game("black", (6,5))
game.print_board()
game.play_game("white", (4,6))
game.print_board()
game.play_game("black", (3,3))
game.print_board()



