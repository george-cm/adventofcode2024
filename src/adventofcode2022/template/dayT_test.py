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


INPUT_S: str = """"""


def test_sove_part1() -> None:
    # assert solve_part1(INPUT_S) ==
    ...


def test_solve_part2() -> None:
    # assert solve_part2(INPUT_S) ==
    ...


if __name__ == "__main__":
    pytest.main(["-vv", "-s"])
