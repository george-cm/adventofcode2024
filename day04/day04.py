from pathlib import Path
from adventofcode.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")


def check_all_directions(x, y, grid):
    sum_total = 0
    width = len(grid[0])
    height = len(grid)
    # check left
    if x+3 < width and all((
        grid[y][x+0] == 'X',
        grid[y][x+1] == 'M',
        grid[y][x+2] == 'A',
        grid[y][x+3] == 'S',
    )):
        sum_total += 1
    # check right
    if x-3 >= 0 and all((
        grid[y][x-0] == 'X',
        grid[y][x-1] == 'M',
        grid[y][x-2] == 'A',
        grid[y][x-3] == 'S',
    )):
        sum_total += 1
    # check down
    if y+3 < height and all((
        grid[y+0][x] == 'X',
        grid[y+1][x] == 'M',
        grid[y+2][x] == 'A',
        grid[y+3][x] == 'S',
    )):
        sum_total += 1
    # check up
    if y-3 >= 0 and all((
        grid[y-0][x] == 'X',
        grid[y-1][x] == 'M',
        grid[y-2][x] == 'A',
        grid[y-3][x] == 'S',
    )):
        sum_total += 1
    # check down-left
    if x+3 < width and y+3 < height and all((
        grid[y+0][x+0] == 'X',
        grid[y+1][x+1] == 'M',
        grid[y+2][x+2] == 'A',
        grid[y+3][x+3] == 'S',
    )):
        sum_total += 1
    # check down-right
    if x-3 >= 0 and y+3 < height and all((
        grid[y+0][x-0] == 'X',
        grid[y+1][x-1] == 'M',
        grid[y+2][x-2] == 'A',
        grid[y+3][x-3] == 'S',
    )):
        sum_total += 1
    # check up-left
    if x+3 < width and y-3 >= 0 and all((
        grid[y-0][x+0] == 'X',
        grid[y-1][x+1] == 'M',
        grid[y-2][x+2] == 'A',
        grid[y-3][x+3] == 'S',
    )):
        sum_total += 1
    # check up-right
    if x-3 >= 0 and y-3 >= 0 and all((
        grid[y-0][x-0] == 'X',
        grid[y-1][x-1] == 'M',
        grid[y-2][x-2] == 'A',
        grid[y-3][x-3] == 'S',
    )):
        sum_total += 1
    return sum_total


def check_x_directions(x, y, grid):
    width = len(grid[0])
    height = len(grid)
    # we need to check the 4 corners of the square around the A (x, y)
    if x == 0 or y == 0 or x == width - 1 or y == height - 1:
        return 0
    c1 = grid[y-1][x-1]
    c2 = grid[y-1][x+1]
    c3 = grid[y+1][x+1]
    c4 = grid[y+1][x-1]
    if sorted([c1, c2, c3, c4]) == ['M', 'M', 'S', 'S'] and c1 != c3:
        return 1
    else:
        return 0


def solve_part1(inputs: str) -> int:
    sum_total = 0

    grid = [list(x) for x in inputs.strip().split("\n")]
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 'X':
                sum_total += check_all_directions(x, y, grid)

    return sum_total


def solve_part2(inputs: str) -> int:
    sum_total = 0

    grid = [list(x) for x in inputs.strip().split("\n")]
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 'A':
                sum_total += check_x_directions(x, y, grid)

    return sum_total


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
