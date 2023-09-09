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

    def __add__(self, other: Position):
        # self.row += other.row
        # self.col += other.col
        return Position(self.row + other.row, self.col + other.col)


class Grid:
    def __init__(
        self, rows: int, cols: int, head_pos: Position, tail_pos: Position
    ) -> None:
        self.rows: int = rows
        self.cols: int = cols
        self.min_row = self.max_row = head_pos.row
        self.min_col = self.max_col = head_pos.col
        self.head_pos: Position = head_pos
        self.tail_pos: Position = tail_pos

    def update_head_position(self, pos: Position) -> None:
        if pos.row > self.max_row:
            self.max_row = pos.row
        if pos.row < self.min_row:
            self.min_row = pos.row
        if pos.col > self.max_col:
            self.max_col = pos.col
        if pos.col < self.min_col:
            self.min_col = pos.col
        self.head_pos = pos

    def __str__(self):
        grid: list[list[str]] = []
        grid = [["."] * (self.max_col + 1) for _ in range(self.max_row + 1)]
        grid[0][0] = "s"
        grid[self.head_pos.row][self.head_pos.col] = "H"
        if self.tail_pos != self.head_pos:
            grid[self.tail_pos.row][self.tail_pos.col] = "T"
        return "\n".join([" ".join(row) for row in reversed(grid)])


def solve_part1(inputs: str) -> int:
    result: int = 0
    # write code here, update rusult
    row: int = 0
    col: int = 0
    current_pos: Position = Position(row, col)
    prev_pos: Position = current_pos
    moves: list[str] = inputs.splitlines()
    head_pos: Position = current_pos
    tail_pos: Position = current_pos
    tail_pos_set: set[Position] = {tail_pos}
    grid = Grid(0, 0, head_pos, tail_pos)
    print(grid)
    for move in moves:
        match move.split(" "):
            case ("U", y):
                # row += int(y)
                # current_pos = Position(row, col)
                prev_head_pos = head_pos
                head_pos = prev_head_pos + Position(int(y), 0)
                grid.update_head_position(head_pos)
                print(
                    f"Current pos = {prev_head_pos}, going up {y}, new position = {head_pos}"
                )
                print(grid)
                # prev_pos = current_pos
            case ("D", y):
                # row -= int(y)
                # current_pos = Position(row, col)
                # grid.update_head_position(current_pos)
                prev_head_pos = head_pos
                head_pos = prev_head_pos + Position(-int(y), 0)
                grid.update_head_position(head_pos)
                print(
                    f"Current pos = {prev_head_pos}, going down {y}, new position = {head_pos}"
                )
                print(grid)
                # prev_pos = current_pos
            case ("L", x):
                # col -= int(x)
                # current_pos = Position(row, col)
                # grid.update_head_position(current_pos)
                prev_head_pos = head_pos
                head_pos = prev_head_pos + Position(0, -int(x))
                grid.update_head_position(head_pos)
                print(
                    f"Current pos = {prev_head_pos}, going left {x}, new position = {head_pos}"
                )
                print(grid)
                # prev_pos = current_pos
            case ("R", x):
                # col += int(x)
                # current_pos = Position(row, col)
                # grid.update_head_position(current_pos)
                prev_head_pos = head_pos
                head_pos = prev_head_pos + Position(0, int(x))
                grid.update_head_position(head_pos)
                print(
                    f"Current pos = {prev_head_pos}, going right {x}, new position = {head_pos}"
                )
                print(grid)
                # prev_pos = current_pos

    return result


def solve_part2(inputs: str) -> int:
    result: int = 0
    # write code here, update rusult

    return result


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
