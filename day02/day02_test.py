from pathlib import Path

from adventofcode.common import load_input
from day02 import solve_part1, solve_part2  # type: ignore

INPUT_S: str = load_input(Path(__file__).parent / "example.txt")


def test_solve_part1():
    assert solve_part1(INPUT_S) == 2


def test_solve_part2():
    assert solve_part2(INPUT_S) == 4
