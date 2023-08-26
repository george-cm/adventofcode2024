import sys
from importlib import util
from importlib.machinery import ModuleSpec
from pathlib import Path
from types import ModuleType

import pytest

full_path = Path(__file__)
file_path: Path = full_path.parent / full_path.name.replace("_test", "")
module_name: str = file_path.stem

spec: ModuleSpec | None = util.spec_from_file_location(module_name, file_path)
module: ModuleType = util.module_from_spec(spec)  # type: ignore
spec.loader.exec_module(module)  # type: ignore
sys.modules["solutions"] = module

from solutions import calculate_priority  # type: ignore  # noqa: E402
from solutions import solve_part1, solve_part2

INPUT_S: str = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def banner(msg: str) -> str:
    return f"\n{'=' * len(msg)}{msg}{'-' * len(msg)}"


def test_calculate_priority() -> None:
    assert calculate_priority("a") == 1
    assert calculate_priority("b") == 2
    assert calculate_priority("c") == 3
    assert calculate_priority("x") == 24
    assert calculate_priority("y") == 25
    assert calculate_priority("z") == 26
    assert calculate_priority("A") == 27
    assert calculate_priority("B") == 28
    assert calculate_priority("C") == 29
    assert calculate_priority("X") == 50
    assert calculate_priority("Y") == 51
    assert calculate_priority("Z") == 52


def test_sove_part1() -> None:
    assert solve_part1(INPUT_S) == 157


def test_solve_part2() -> None:
    assert solve_part2(INPUT_S) == 70


if __name__ == "__main__":
    pytest.main(["-vv", "-s"])
