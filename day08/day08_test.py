import pytest

from day08 import tree_seenic_score  # type: ignore  # noqa: E402
from day08 import create_grid, solve_part1, solve_part2  # type: ignore  # noqa: E402

INPUT_S: str = """30373
25512
65332
33549
35390"""


def test_tree_scenic_score():
    tree = (1, 2)
    grid = create_grid(INPUT_S)
    scenic_score = tree_seenic_score(tree, grid)
    assert scenic_score == 4


def test_solve_part1() -> None:
    assert solve_part1(INPUT_S) == 21


def test_solve_part2() -> None:
    assert solve_part2(INPUT_S) == 8


if __name__ == "__main__":
    pytest.main(["-vv", "-s", __file__])
