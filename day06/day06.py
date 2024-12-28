from enum import Enum
from pathlib import Path

from adventofcode.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


def display_grid(grid: list[list[str]]) -> None:
    print("  " + " ".join([str(x) for x in list(range(0, len(grid[0])))]))
    for line_no, line in enumerate(grid):
        print(line_no, " ".join(line))
    print()


def solve_part1(inputs: str) -> int:
    grid: list[list[str]] = [list(x) for x in inputs.strip().split("\n")]
    heigth = len(grid)
    width = len(grid[0])

    distinct_guard_positions: set[tuple[int, int]] = set()
    current_direction = Direction.UP
    guard_y: int = [y for y, c in enumerate(grid) if "^" in c][0]
    guard_x: int = grid[guard_y].index("^")
    display_grid(grid)
    print(guard_x, guard_y)
    guard_inside_grid = True
    while guard_inside_grid:
        distinct_guard_positions.add((guard_x, guard_y))
        match current_direction:
            case Direction.UP:
                next_x = guard_x
                next_y = guard_y - 1
            case Direction.RIGHT:
                next_x = guard_x + 1
                next_y = guard_y
            case Direction.DOWN:
                next_x = guard_x
                next_y = guard_y + 1
            case Direction.LEFT:
                next_x = guard_x - 1
                next_y = guard_y

        if next_y < 0 or next_y == heigth or next_x < 0 or next_x == width:
            # outside the grid
            guard_inside_grid = False
        else:
            c = grid[next_y][next_x]
            if c == "#":
                current_direction = Direction(
                    (current_direction.value + 1) % len(Direction)
                )
            else:
                # move the guard to the next location
                guard_x = next_x
                guard_y = next_y
    return len(distinct_guard_positions)


def solve_part2(inputs: str) -> int:
    result: int = 0
    # write code here, update result

    return result


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
