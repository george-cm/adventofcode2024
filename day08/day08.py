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
    # pprint(grid)
    # print(f"tree value {grid[tree[0]][tree[1]]}")
    # print(f"{tree=}")
    # print(f"{row=}")
    # print(f"{col=}")
    tree_value: int = grid[tree[0]][tree[1]]
    return (
        tree_value > max(row[: tree[1]])
        or tree_value > max(row[tree[1] + 1 :])
        or tree_value > max(col[: tree[0]])
        or tree_value > max(col[tree[0] + 1 :])
    )


def calculate_perimeter(grid: list[list[int]]) -> int:
    return 4 * len(grid) - 4


def solve_part1(inputs: str) -> int:
    # write code here, update rusult
    grid: list[list[int]] = create_grid(inputs)
    count_visible_trees: int = calculate_perimeter(grid)
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid) - 1):
            # print(
            #     f"tree {row},{col} is visible? {is_tree_visible((row, col), grid)}"
            # )
            if is_tree_visible((row, col), grid):
                count_visible_trees += 1
    return count_visible_trees


def solve_part2(inputs: str) -> int:
    result: int = 0
    # write code here, update rusult

    return result


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
