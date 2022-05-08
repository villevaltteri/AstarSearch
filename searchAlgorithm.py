from typing import List, Tuple


class AStarSearch:
    def __init__(self, path: str) -> None:
        self._path = path
        self._open_list = []
        self._end_point = None
        self._start_point = None
        self._board: List[List[int]] = []

    def _heuristic(self, y: int, x: int) -> int:
        return abs(self._end_point[0] - y) + abs(self._end_point[1] - x)

    def _add_to_open_list(self, y: int, x: int, g: int, h: int) -> None:
        self._open_list.append([y, x, g, h])

    def _sort_open_points(self) -> None:
        self._open_list.sort(key=lambda x: x[2] + x[3], reverse=True)

    def _check_valid_point(self, y: int, x: int) -> bool:
        valid_y = (0 <= y < len(self._board))
        valid_x = (0 <= x < len(self._board[0]))
        if valid_y and valid_x:
            return self._board[y][x] == 0
        return False

    def _expand_neighbour_points(self, current: List[int]) -> None:
        delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(len(delta)):
            y2 = current[0] + delta[i][0]
            x2 = current[1] + delta[i][1]
            if self._check_valid_point(y2, x2):
                g2 = current[2] + 1
                h2 = self._heuristic(y2, x2)
                self._board[y2][x2] = 4
                self._add_to_open_list(y2, x2, g2, h2)

    def search(self) -> None:
        y = self._start_point[0]
        x = self._start_point[1]
        g = 0
        h = self._heuristic(y, x)
        self._add_to_open_list(y, x, g, h)
        while self._open_list:
            self._sort_open_points()
            current_point = self._open_list.pop()
            y = current_point[0]
            x = current_point[1]
            self._board[y][x] = 2
            if y == self._end_point[0] and x == self._end_point[1]:
                for i in range(len(self._board)):
                    for j in range(len(self._board[0])):
                        print(f"{self._board[i][j]:<4}", end="")
                    print()
            self._expand_neighbour_points(current_point)

    def load_board(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        try:
            with open(self._path, 'r') as file:
                while line := file.readline():
                    self._board.append([int(c) for c in line if c.isalnum()])
        except FileNotFoundError as e:
            print(f"{e.strerror}: {e.filename} didn't match any file. Check the path name")
        self._end_point = end
        self._start_point = start


if __name__ == "__main__":
    path = "./map.txt"
    solver = AStarSearch(path)
    solver.load_board((0, 0), (5, 6))
    solver.search()