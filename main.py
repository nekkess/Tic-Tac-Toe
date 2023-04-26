data = [
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
]


class TicTacToe:

    def move(self):
        if self.number_of_turns == 1:
            table = f"{data[0][0]}|{data[0][1]}|{data[0][2]}\n" \
                    f"-----------\n" \
                    f"{data[1][0]}|{data[1][1]}|{data[1][2]}\n" \
                    f"-----------\n" \
                    f"{data[2][0]}|{data[2][1]}|{data[2][2]}\n"
            print(table)

        row_chosen = int(input('Choose a row: ')) - 1
        column_chosen = int(input('Choose a column: ')) - 1

        if int(self.number_of_turns) % 2 != 0:
            data[row_chosen][column_chosen] = ' X '
        else:
            data[row_chosen][column_chosen] = ' O '

        table_renewed = f"{data[0][0]}|{data[0][1]}|{data[0][2]}\n" \
                        f"-----------\n" \
                        f"{data[1][0]}|{data[1][1]}|{data[1][2]}\n" \
                        f"-----------\n" \
                        f"{data[2][0]}|{data[2][1]}|{data[2][2]}\n"
        print(table_renewed)
        self.number_of_turns += 1
        if self.number_of_turns == 10:
            self.game_is_on = False
            print("Game Over! It's a draw!")
        self.check_if_end()

    def __init__(self):
        self.game_is_on = True
        self.number_of_turns = 1
        while self.game_is_on:
            self.move()

    def check_if_end(self):
        for row in data:
            if ''.join(row) == ' X  X  X ':
                print('X player wins!')
                self.game_is_on = False
            elif ''.join(row) == ' O  O  O ':
                print('O player wins!')
                self.game_is_on = False

        for section in data[0]:
            if section != '   ':
                if data[0][0] == ' X ' and data[1][0] == ' X ' and data[2][0] == ' X ':
                    print('X player wins!')
                    self.game_is_on = False
                elif data[0][0] == ' O ' and data[1][0] == ' O ' and data[2][0] == ' O ':
                    print('O player wins!')
                    self.game_is_on = False
                elif data[0][1] == ' X ' and data[1][1] == ' X ' and data[2][1] == ' X ':
                    print('X player wins!')
                    self.game_is_on = False
                elif data[0][1] == ' O ' and data[1][1] == ' O ' and data[2][1] == ' O ':
                    print('O player wins!')
                    self.game_is_on = False
                elif data[0][2] == ' X ' and data[1][2] == ' X ' and data[2][2] == ' X ':
                    print('X player wins!')
                    self.game_is_on = False
                elif data[0][2] == ' O ' and data[1][2] == ' O ' and data[2][2] == ' O ':
                    print('O player wins!')
                    self.game_is_on = False

        if data[0][0] != '   ' or data[2][2] != '   ':
            # check diagonal starting left top
            if data[0][0] == ' X ' and data[1][1] == ' X ' and data[2][2] == ' X ':
                print('X player wins!')
                self.game_is_on = False
            elif data[0][0] == ' O ' and data[1][1] == ' O ' and data[2][2] == ' O ':
                print('O player wins!')
                self.game_is_on = False
            # check diagonal starting right top
            if data[0][2] == ' X ' and data[1][1] == ' X ' and data[2][0] == ' X ':
                print('X player wins!')
                self.game_is_on = False
            elif data[0][2] == ' O ' and data[1][1] == ' O ' and data[2][0] == ' O ':
                print('O player wins!')
                self.game_is_on = False


game = TicTacToe()
