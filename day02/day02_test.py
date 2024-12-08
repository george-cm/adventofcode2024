from pathlib import Path

from adventofcode.common import load_input
from day02 import part1, part2  # type: ignore

INPUT_S: str = load_input(Path(__file__).parent / "example.txt")


def test_part1():
    assert part1(INPUT_S) == 2


def test_part2():
    assert part2(INPUT_S) == 4
