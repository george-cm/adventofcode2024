from importlib.machinery import ModuleSpec
from pathlib import Path
import sys
from importlib import util
from types import ModuleType

import pytest

full_path = Path(__file__)
file_path: Path = full_path.parent / (full_path.name.replace("_test", ""))
module_name: str = file_path.stem

spec: ModuleSpec | None = util.spec_from_file_location(module_name, file_path)
module: ModuleType = util.module_from_spec(spec)  # type: ignore
spec.loader.exec_module(module)  # type: ignore
sys.modules["solutions"] = module

from solutions import solve_part1, solve_part2  # type: ignore  # noqa: E402


INPUT_S: str = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def test_solve_part1() -> None:
    assert solve_part1(INPUT_S) == 2


def test_solve_part2() -> None:
    assert solve_part2(INPUT_S) == 4


if __name__ == "__main__":
    pytest.main(["-vv", "-s"])
