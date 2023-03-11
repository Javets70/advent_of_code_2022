from pprint import pprint


def dict_matrix(board: list):
    dic = {}
    matrix = [list(map(int, i.split())) for i in board]

    for i in range(len(matrix)):
        dic[i] = {}
        for j in range(len(matrix)):
            dic[i][matrix[i][j]] = False
    return dic


def update_board(dic: dict, num: int):
    for key in dic:
        for d in dic[key]:
            if d == num:
                dic[key][d] = True


def check_bingo(dic: dict):
    # checking rows
    for d in dic.values():  # d stores a dict
        if sum(list(d.values())) == 5:
            return True

    return False


data = open("./day4_sample_input.txt").read()
bingo_numbers = list(map(int, data.split("\n")[0].split(",")))

board_blocks = data.split("\n")[1:]
boards = {}
for i in range(len(board_blocks) - 5):
    if not (board_blocks[i]):  # check if its empty string
        board = board_blocks[i + 1: i + 6]
        boards[i // 6] = dict_matrix(board)

print(boards[0])
pprint(boards[0])
