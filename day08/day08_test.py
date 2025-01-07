from pathlib import Path

import pytest

from adventofcode.common import load_input
from day08 import (
    create_grid,
    create_pairs,
    find_antennae,
    solve_part1,
    solve_part2,
)

INPUT_S: str = load_input(Path(__file__).parent / "example.txt")


def test_create_grid():
    inputs = """..0.
A...
.B.."""
    grid = create_grid(inputs)
    assert grid == [
        [".", ".", "0", "."],
        ["A", ".", ".", "."],
        [".", "B", ".", "."],
    ]


def test_find_antennae():
    inputs = """..0.
A.0.
.B.A"""
    grid = create_grid(inputs)
    antennae = find_antennae(grid)
    assert antennae == {
        "0": [(2, 0), (2, 1)],
        "A": [(0, 1), (3, 2)],
        "B": [(1, 2)],
    }


def test_create_pairs():
    locations = [(2, 0), (2, 1), (1, 3), (3, 0)]
    pairs = create_pairs(locations)
    # print(pairs)
    assert pairs == [
        ((2, 0), (2, 1)),
        ((1, 3), (2, 0)),
        ((2, 0), (3, 0)),
        ((1, 3), (2, 1)),
        ((2, 1), (3, 0)),
        ((1, 3), (3, 0)),
    ]


def test_solve_part1() -> None:
    assert solve_part1(INPUT_S) == 14


def test_solve_part2() -> None:
    assert solve_part2(INPUT_S) == 34


if __name__ == "__main__":
    pytest.main(["-vv", "-s", __file__])
