class Game:
    score_points = 0
    def __init__(self):
        self.board = ["-"] * 9
        self.game_on = True
        self.current_player = "x"

    def display_board(self):
        b = self.board
        print()
        print(b[0] + " | " + b[1] + " | " + b[2] + "       1 | 2 | 3")
        print(b[3] + " | " + b[4] + " | " + b[5] + "       4 | 5 | 6")
        print(b[6] + " | " + b[7] + " | " + b[8] + "       7 | 8 | 9")
        print()

    def player(self):
        while True:
            p1 = input("player 1,  Choose Player `X` Or `O`: ").strip().lower()
            if p1.upper() in ["X", "O"]:
                self.current_player = p1.upper()
                break
            else:
                print("Invalid input. Enter X or O to select player.")

    def player_position(self):
        while True:
            position = input(
                f"{self.current_player}'s Turn, Choose Position (1-9): "
            ).strip()
            if position in [str(i) for i in range(1, 10)]:
                position = int(position) - 1

                if self.board[position] == "-":
                    self.board[position] = self.current_player
                    break
                else:
                    print("That position is already taken. ")

            else:
                print("Invalid input. Choose number between (1-9).")

    def check_winner(self):
        win_patterens = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

        for pattern in win_patterens:
            if (
                self.board[pattern[0]]
                == self.board[pattern[1]]
                == self.board[pattern[2]]
                != "-"
            ):
                self.score_points += 10
                print(f"Congratulation `{self.board[pattern[0]]}` wins! \n Score: {self.score_points}")
                self.game_on = False
                return

        if "-" not in self.board:
            self.display_board()
            print("It's Tie.")
            self.game_on = False

    def flip_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play_game(self):
        self.board = ['-'] * 9
        self.current_player = "X"
        self.game_on = True

        print("Welcome to Tic Tac Toe Game!. ")
        self.display_board()
        self.player()

        while self.game_on:
            self.display_board()
            self.player_position()
            self.check_winner()

            if self.game_on:
                self.flip_player()

while True:
    game = Game()
    game.play_game()

    play_again = input("Would you like to play again? ").lower().strip()
    if play_again != "yes":
        print("\nThanks to play this game. ")
        break
