from dataclasses import dataclass
from pathlib import Path

from adventofcode2022.common import load_input

# from typing import TypeVar


INPUT_S: str = load_input(Path(__file__).parent / "input.txt")

# Position = TypeVar("Position")


@dataclass(frozen=True)
class Position:
    row: int
    col: int

    def __add__(self, other: "Position") -> "Position":
        return Position(self.row + other.row, self.col + other.col)

    def __sub__(self, other: "Position") -> "Position":
        return Position(self.row - other.row, self.col - other.col)

    def _eq_(self, other: "Position") -> bool:
        return all((self.row == other.row, self.col == other.col))

    def __abs__(self) -> "Position":
        return Position(abs(self.row), abs(self.col))

    def __gt__(self, other: "Position") -> bool:
        return any((self.row > other.row, self.col > other.col))

    def swap(self):
        return Position(self.col, self.row)


class Grid:
    def __init__(
        self,
        rows: int,
        cols: int,
        head_pos: Position,
        segments: int = 2,
        visualize: bool = False,
        padding_rows: int = 0,
        padding_cols: int = 0,
    ) -> None:
        self.rows: int = rows
        self.cols: int = cols
        self.min_row = self.max_row = 5
        self.min_col = self.max_col = 5
        self.head_pos: Position = head_pos
        self.segments: list[Position] = [head_pos for _ in range(segments)]
        self.tail_visited_positions: list[Position] = [self.segments[-1]]
        self.visualize = visualize
        self.padding_rows = padding_rows
        self.padding_cols = padding_cols

    def _parse_move(self, move_instruction: str) -> tuple[Position, int]:
        split_move_instruction: list[str] = move_instruction.split(" ")
        move: tuple[str, int] = (
            split_move_instruction[0],
            int(split_move_instruction[1]),
        )
        if self.visualize:
            print(f"{move=}")
        direction: Position
        match move:
            case ("R", steps):
                direction = Position(0, 1)
            case ("L", steps):
                direction = Position(0, -1)
            case ("U", steps):
                direction = Position(1, 0)
            case ("D", steps):
                direction = Position(-1, 0)
            case _:
                raise NotImplementedError(f"{move_instruction=} not implemented.")
        return direction, steps

    def move_segments(self, move_instruction: str) -> None:
        if self.visualize:
            print(f"========= Moving {move_instruction} =========")
            print("Starting position:")
            print(self)
            print()
        if self.visualize:
            print("moving:")
        direction: Position
        steps: int
        direction, steps = self._parse_move(move_instruction)
        for _ in range(steps):
            # self.head_pos += direction
            self.segments[0] += direction
            self.update_grid_size()
            # delta: Position = self.segments[0] - self.segments[1]
            # to_move: Position = delta - direction
            # move all the remaining segments
            for i in range(1, len(self.segments)):
                segments_delta = self.segments[i - 1] - self.segments[i]
                if abs(segments_delta) > Position(1, 1):
                    # self.segments[i] += segments_delta - direction
                    self.segments[i] += self._clamp(segments_delta)
                    # self.segments[i] += to_move
                    if i == len(self.segments) - 1:
                        self.tail_visited_positions.append(self.segments[i])
            if self.visualize:
                print(self)
                print()

    def _clamp(
        self, pos: Position, min_value: int = -1, max_value: int = 1
    ) -> Position:
        row: int = max(min(pos.row, max_value), min_value)
        col: int = max(min(pos.col, max_value), min_value)
        return Position(row, col)

    def unique_tail_positions(self):
        return set(self.tail_visited_positions)

    def update_grid_size(self) -> None:
        self.max_row = max(self.segments[0].row, self.max_row)
        self.min_row = min(self.segments[0].row, self.min_row)
        self.max_col = max(self.segments[0].col, self.max_col)
        self.min_col = min(self.segments[0].col, self.min_col)

    def visited_tail_positions(self) -> str:
        grid: list[list[str]] = []
        max_pos = self._normalize_pos(Position(self.max_row, self.max_col))
        grid = [
            ["."] * (max_pos.col + self.padding_cols + 1)
            for _ in range(max_pos.row + self.padding_rows + 1)
        ]

        for pos in self.unique_tail_positions():
            norm_pos = self._normalize_pos(pos)
            grid[norm_pos.row][norm_pos.col] = "#"
        norm_origin = self._normalize_pos(Position(0, 0))
        grid[norm_origin.row][norm_origin.col] = "s"
        return "\n".join([" ".join(row) for row in reversed(grid)])

    def _normalize_pos(self, pos: Position) -> Position:
        return pos + abs(Position(min(self.min_row, 0), min(self.min_col, 0)))

    def __str__(self) -> str:
        # print(f"{self.max_row=}, {self.max_col=}")
        grid: list[list[str]] = []
        max_pos = self._normalize_pos(Position(self.max_row, self.max_col))
        grid = [
            ["."] * (max_pos.col + self.padding_cols + 1)
            for _ in range(max_pos.row + self.padding_rows + 1)
        ]
        grid[0][0] = "s"
        for i, pos in enumerate(reversed(self.segments)):
            norm_pos = self._normalize_pos(pos)
            # print(f"segment: {len(self.segments) - 1 - i} {norm_pos=}")
            grid[norm_pos.row][norm_pos.col] = str(len(self.segments) - 1 - i)
        norm_head_pos = self._normalize_pos(self.segments[0])
        grid[norm_head_pos.row][norm_head_pos.col] = "H"
        return "\n".join([" ".join(row) for row in reversed(grid)])


def solve_part1(inputs: str, visualize: bool = False) -> int:
    # result: int = 0
    # write code here, update rusult
    row: int = 0
    col: int = 0
    current_pos: Position = Position(row, col)
    moves: list[str] = inputs.splitlines()
    head_pos: Position = current_pos
    # tail_pos: Position = current_pos
    grid = Grid(0, 0, head_pos, 2, visualize=visualize)
    for move in moves:
        grid.move_segments(move)
    if visualize:
        print(grid.visited_tail_positions())
    return len(grid.unique_tail_positions())


def solve_part2(inputs: str, visualize: bool = False) -> int:
    # result: int = 0
    # write code here, update rusult
    row: int = 0
    col: int = 0
    current_pos: Position = Position(row, col)
    moves: list[str] = inputs.splitlines()
    head_pos: Position = current_pos
    # tail_pos: Position = current_pos
    grid = Grid(0, 0, head_pos, 10, visualize=visualize)
    for move in moves:
        grid.move_segments(move)
    if visualize:
        print(grid.visited_tail_positions())
    return len(grid.unique_tail_positions())


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
