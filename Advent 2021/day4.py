from pprint import pprint


def dict_matrix(board: list):
    dic = {}
    matrix = [list(map(int, i.split())) for i in board]

    for i in range(len(matrix)):
        dic[i] = {}
        for j in range(len(matrix)):
            dic[i][j] = [matrix[i][j], False]
    return dic


def update_board(dic: dict, num: int):
    for i in range(5):
        for j in range(5):
            if dic[i][j][0] == num:
                dic[i][j][1] = True


def check_bingo(dic: dict):
    # checking rows
    for value in dic.values():
        row_values = [i[1] for i in value.values()]
        if sum(row_values) == 5:
            return True

    # checking columns
    for i in range(5):
        column = []
        for j in range(5):
            column.append(dic[j][i][1])
        if sum(column) == 5:
            return True

    return False


def calc_score(dic: dict, num: int):
    unmarked_nums = []
    for i in range(5):
        for j in range(5):
            if dic[i][j][1] is False:
                unmarked_nums.append(dic[i][j][0])
    return sum(unmarked_nums) * num


data = open("./day4_input.txt").read()
bingo_numbers = list(map(int, data.split("\n")[0].split(",")))

board_blocks = data.split("\n")[1:]
boards = {}
for i in range(len(board_blocks) - 5):
    if not (board_blocks[i]):  # check if its empty string
        board = board_blocks[i + 1: i + 6]
        boards[i // 6] = dict_matrix(board)

winning_boards = []
just_called_num = 0

for bingo_number in bingo_numbers:
    just_called_num = bingo_number
    for board_number in boards:
        update_board(boards[board_number], bingo_number)
        if check_bingo(boards[board_number]):
            if board_number not in winning_boards:
                winning_boards.append(board_number)

    if len(winning_boards) == len(boards):
        break

print(winning_boards)
print(just_called_num)
print("DAY4 PART2", calc_score(boards[winning_boards[-1]], just_called_num))
