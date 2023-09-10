from dataclasses import dataclass
from pathlib import Path
from typing import TypeVar

from adventofcode2022.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")

Position = TypeVar("Position")


@dataclass(frozen=True)
class Position:
    row: int
    col: int

    def __add__(self, other: Position) -> Position:
        return Position(self.row + other.row, self.col + other.col)

    def __sub__(self, other: Position) -> Position:
        return Position(self.row - other.row, self.col - other.col)

    def _eq_(self, other: Position) -> bool:
        return all(self.row == other.row, self.col == other.col)

    def __abs__(self) -> Position:
        return Position(abs(self.row), abs(self.col))

    def __gt__(self, other: Position) -> bool:
        return any(self.row > other.row, self.col > other.col)


class Grid:
    def __init__(
        self, rows: int, cols: int, head_pos: Position, tail_pos: Position
    ) -> None:
        self.rows: int = rows
        self.cols: int = cols
        self.min_row = self.max_row = 5
        self.min_col = self.max_col = 5
        self.head_pos: Position = head_pos
        self.tail_pos: Position = tail_pos
        self.tail_visited_positions: list[Position] = [self.tail_pos]

    def move_head(self, move_instruction: str) -> None:
        print(f"========= Moving {move_instruction} =========")
        print("Starting position:")
        print(self)
        print()
        split_move_instruction: list[str] = move_instruction.split(" ")
        move: tuple[str, int] = (
            split_move_instruction[0],
            int(split_move_instruction[1]),
        )
        # print(f"{move=}")
        match move:
            case ("R", x):
                direction: Position = Position(0, 1)
            case ("L", x):
                direction: Position = Position(0, -1)
            case ("U", x):
                direction: Position = Position(1, 0)
            case ("D", x):
                direction: Position = Position(-1, 0)
            case _:
                raise NotImplementedError(
                    f"{move_instruction=} not implemented.")

        print("moving:")
        for _ in range(x):
            self.head_pos += direction
            self.update_grid_size()
            head_tail_delta = self.head_pos - self.tail_pos
            if any(
                (
                    abs(head_tail_delta) == Position(1, 2),
                    abs(head_tail_delta) == Position(2, 1),
                    abs(head_tail_delta) == Position(0, 2),
                    abs(head_tail_delta) == Position(2, 0),
                )
            ):
                self.tail_pos += head_tail_delta - direction
                self.tail_visited_positions.append(self.tail_pos)
            print(self)
            print()

    def unique_tail_positions(self):
        return set(self.tail_visited_positions)

    def update_grid_size(self) -> None:
        self.max_row = max(self.head_pos.row, self.max_row)
        self.min_row = min(self.head_pos.row, self.min_row)
        self.max_col = max(self.head_pos.col, self.max_col)
        self.min_col = min(self.head_pos.col, self.max_col)

    def update_head_position(self, pos: Position) -> None:
        self.max_row = max(pos.row, self.max_row)
        self.min_row = min(pos.row, self.min_row)
        self.max_col = max(pos.col, self.max_col)
        self.min_col = min(pos.col, self.max_col)
        prev_head_pos: Position = self.head_pos
        self.head_pos = pos
        head_tail_delta: Position = self.head_pos - self.tail_pos

        print()
        print(
            f"head = {self.head_pos} -- tail = {self.tail_pos} -- detla = {head_tail_delta}"
        )

    def visited_tail_positions(self) -> str:
        grid: list[list[str]] = []
        grid = [["."] * (self.max_col + 1) for _ in range(self.max_row + 1)]

        for pos in self.unique_tail_positions():
            grid[pos.row][pos.col] = "#"
        return "\n".join([" ".join(row) for row in reversed(grid)])

    def __str__(self) -> str:
        grid: list[list[str]] = []
        grid = [["."] * (self.max_col + 1) for _ in range(self.max_row + 1)]
        grid[0][0] = "s"
        grid[self.head_pos.row][self.head_pos.col] = "H"
        if self.tail_pos != self.head_pos:
            grid[self.tail_pos.row][self.tail_pos.col] = "T"
        return "\n".join([" ".join(row) for row in reversed(grid)])


def solve_part1(inputs: str) -> int:
    # result: int = 0
    # write code here, update rusult
    row: int = 0
    col: int = 0
    current_pos: Position = Position(row, col)
    moves: list[str] = inputs.splitlines()
    head_pos: Position = current_pos
    tail_pos: Position = current_pos
    grid = Grid(0, 0, head_pos, tail_pos)
    for move in moves:
        grid.move_head(move)
    print(grid.visited_tail_positions())
    return len(grid.unique_tail_positions())


def solve_part2(inputs: str) -> int:
    result: int = 0
    # write code here, update rusult

    return result


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
