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


def will_loop(grid: list[list[str]], guard_x: int, guard_y: int) -> bool:
    heigth = len(grid)
    width = len(grid[0])
    orig_guard_x = guard_x
    orig_guard_y = guard_y
    distinct_guard_positions: set[tuple[int, int, Direction]] = set()
    current_direction: Direction = Direction.UP
    loop: bool = False
    while True:
        grid[orig_guard_y][orig_guard_x] = "^"
        if (guard_x, guard_y, current_direction) in distinct_guard_positions:
            loop = True
            # print("LOOP")
            # display_grid(grid)
            return loop
        distinct_guard_positions.add((guard_x, guard_y, current_direction))
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
            break
        c = grid[next_y][next_x]
        if c == "#" or c == "O":
            current_direction = Direction(
                (current_direction.value + 1) % len(Direction)
            )
            grid[guard_y][guard_x] = "+"
        else:
            # move the guard to the next location
            guard_x = next_x
            guard_y = next_y
            match current_direction:
                case Direction.UP | Direction.DOWN:
                    grid[guard_y][guard_x] = "|"
                case Direction.LEFT | Direction.RIGHT:
                    grid[guard_y][guard_x] = "-"
    # print("NO LOOP")
    # display_grid(grid)
    return loop


def get_distinct_positions(
    grid: list[list[str]], guard_x: int, guard_y: int
) -> set[tuple[int, int]]:
    heigth = len(grid)
    width = len(grid[0])

    distinct_guard_positions: set[tuple[int, int]] = set()
    current_direction = Direction.UP
    while True:
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
            break
        c = grid[next_y][next_x]
        if c == "#":
            current_direction = Direction(
                (current_direction.value + 1) % len(Direction)
            )
        else:
            # move the guard to the next location
            guard_x = next_x
            guard_y = next_y
    return distinct_guard_positions


def solve_part1(inputs: str) -> int:
    grid: list[list[str]] = [list(x) for x in inputs.strip().split("\n")]
    guard_y: int = [y for y, c in enumerate(grid) if "^" in c][0]
    guard_x: int = grid[guard_y].index("^")
    distinct_guard_positions: set[tuple[int, int]] = get_distinct_positions(
        grid, guard_x, guard_y
    )
    return len(distinct_guard_positions)


def solve_part2(inputs: str) -> int:
    grid: list[list[str]] = [list(x) for x in inputs.strip().split("\n")]
    # display_grid(grid)
    guard_y: int = [y for y, c in enumerate(grid) if "^" in c][0]
    guard_x: int = grid[guard_y].index("^")
    distinct_guard_positions: set[tuple[int, int]] = get_distinct_positions(
        grid, guard_x, guard_y
    )
    loops: int = 0
    for x, y in distinct_guard_positions:
        grid_to_check: list[list[str]] = [[x for x in line] for line in grid]
        grid_to_check[y][x] = "O"
        if will_loop(grid_to_check, guard_x, guard_y):
            loops += 1
    return loops


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
