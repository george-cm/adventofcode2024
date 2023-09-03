from pathlib import Path

from adventofcode2022.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")


def create_grid(inputs: str) -> list[list[int]]:
    lines = inputs.splitlines()
    return [list(map(int, line)) for line in lines]


def get_row(row: int, grid: list[list[int]]) -> list[int]:
    return grid[row]


def get_col(col: int, grid: list[list[int]]) -> list[int]:
    return [row[col] for row in grid]


def is_tree_visible(tree: tuple[int, int], grid: list[list[int]]) -> bool:
    row: list[int] = get_row(tree[0], grid)
    col: list[int] = get_col(tree[1], grid)
    tree_value: int = grid[tree[0]][tree[1]]
    return (
        tree_value > max(row[: tree[1]])
        or tree_value > max(row[tree[1] + 1 :])
        or tree_value > max(col[: tree[0]])
        or tree_value > max(col[tree[0] + 1 :])
    )


def calculate_perimeter(grid: list[list[int]]) -> int:
    # return 4 * len(grid) - 4
    return (2 * len(grid)) + (2 * (len(grid[0]) - 2))


def tree_seenic_score(tree: tuple[int, int], grid: list[list[int]]):
    row: list[int] = get_row(tree[0], grid)
    col: list[int] = get_col(tree[1], grid)
    tree_value: int = grid[tree[0]][tree[1]]

    # look left
    left_visibility = 0
    for other_tree in reversed(row[: tree[1]]):
        left_visibility += 1
        if other_tree >= tree_value:
            break

    # look right
    right_visibility = 0
    for other_tree in row[tree[1] + 1 :]:
        right_visibility += 1
        if other_tree >= tree_value:
            break

    # look up
    up_visibility = 0
    for other_tree in reversed(col[: tree[0]]):
        up_visibility += 1
        if other_tree >= tree_value:
            break

    # look down
    down_visibility = 0
    for other_tree in col[tree[0] + 1 :]:
        down_visibility += 1
        if other_tree >= tree_value:
            break

    return left_visibility * right_visibility * up_visibility * down_visibility


def solve_part1(inputs: str) -> int:
    # write code here, update rusult
    grid: list[list[int]] = create_grid(inputs)
    count_visible_trees: int = calculate_perimeter(grid)
    row_range = range(1, len(grid[0]) - 1)
    col_range = range(1, len(grid) - 1)
    count_visible_trees += sum(
        is_tree_visible((row, col), grid) for row in row_range for col in col_range
    )
    return count_visible_trees


def solve_part2(inputs: str) -> int:
    # write code here, update rusult
    grid: list[list[int]] = create_grid(inputs)
    row_range = range(len(grid[0]))
    col_range = range(len(grid))
    return max(
        tree_seenic_score((row, col), grid) for row in row_range for col in col_range
    )


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
