from typing import List, Tuple
from userExceptions import BoardEmpty


def check_valid_cell(y: int, x: int, board: List[List[int]]) -> bool:
    valid_y: bool = (0 <= y < len(board))
    valid_x: bool = (0 <= x < len(board[0]))
    if valid_y and valid_x:
        return board[valid_y][valid_x] == 0
    return False


def expand_neighbours(best_option: List[int], board: List[List[int]], open_points: List[List[int]]) -> None:
    delta: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    y = best_option[0]
    x = best_option[1]
    h = best_option[2]
    g = best_option[3]
    for i in range(len(delta)):
        new_y = y + delta[i][0]
        new_x = x + delta[i][1]
        if check_valid_cell(new_y, new_x, board):



def sort_points(open_points: List[List[int]]) -> List[List[int]]:
    open_points.sort(key=lambda x: x[2] + x[3], reverse=True)
    return open_points


def heuristic(y: int, x: int, y2: int, x2: int) -> int:
    return abs(y2-y) + abs(x2-x)


def search(board: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> List[List[int]]:
    open_points: List[List[int]] = []
    y = start[0]
    x = start[1]
    h = heuristic(y, x, end[0], end[1])
    g = 0
    open_points.append([y, x, h, g])
    while not is_board_empty(open_points):
        open_points = sort_points(open_points)
        best_option: List[int] = open_points.pop()
        new_y = best_option[0]
        new_x = best_option[1]
        board[new_y][new_x] = 2
        if new_y == end[0] and new_x == end[1]:
            board[end[0]][end[1]] = 2
            return board
        expand_neighbours(best_option, board, open_points)


def print_board(board: List[List[int]]) -> None:
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()


def is_board_empty(board: List[List[int]]) -> bool:
    return all(map(is_board_empty, board)) if isinstance(board, list) else False


def parse_row(line: str) -> List[int]:
    line = line.strip()
    row: List[int] = [int(n) for n in line if n.isalnum()]
    return row


def load_board(path: str) -> List[List[int]]:
    board: List[List[int]] = []
    with open(path, 'r') as file:
        lines: List[str] = file.readlines()
    for line in lines:
        line = parse_row(line)
        board.append(line)
    if is_board_empty(board):
        raise BoardEmpty("Board is empty. Check the map.txt file")
    return board



path: str = "./map.txt"
mapf = load_board(path)
print_board(mapf)
