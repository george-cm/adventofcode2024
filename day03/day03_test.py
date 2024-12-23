from pathlib import Path

import pytest

from adventofcode.common import load_input
from day03 import solve_part1, solve_part2  # type: ignore  # noqa: E402

INPUT_S: str = load_input(Path(__file__).parent / "example.txt")
INPUT_S2: str = load_input(Path(__file__).parent / "example2.txt")


def test_solve_part1() -> None:
    assert solve_part1(INPUT_S) == 161


def test_solve_part2() -> None:
    assert solve_part2(INPUT_S2) == 48


if __name__ == "__main__":
    pytest.main(["-vv", "-s", __file__])
