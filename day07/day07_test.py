from pathlib import Path

import pytest

from adventofcode.common import load_input
from day07 import (  # type: ignore  # noqa: E402
    create_combination,
    is_valid_calibration,
    parse_input,
    solve_part1,
    solve_part2,
)

INPUT_S: str = load_input(Path(__file__).parent / "example.txt")


def test_parse_input() -> None:
    result = parse_input(INPUT_S)
    assert result == [
        {190: [10, 19]},
        {3267: [81, 40, 27]},
        {83: [17, 5]},
        {156: [15, 6]},
        {7290: [6, 8, 6, 15]},
        {161011: [16, 10, 13]},
        {192: [17, 8, 14]},
        {21037: [9, 7, 18, 13]},
        {292: [11, 6, 16, 20]},
    ]


def test_create_combination_1():
    operators = ("+", "*")
    expected = [["+"], ["*"]]
    result = create_combination(1, operators)
    assert result == expected


def test_create_combination_2():
    operators = ("+", "*")
    expected = [["+", "+"], ["+", "*"], ["*", "+"], ["*", "*"]]
    result = create_combination(2, operators)
    assert result == expected


def test_create_combination_3():
    operators = ("+", "*")
    expected = [
        ["+", "+", "+"],
        ["+", "+", "*"],
        ["+", "*", "+"],
        ["+", "*", "*"],
        ["*", "+", "+"],
        ["*", "+", "*"],
        ["*", "*", "+"],
        ["*", "*", "*"],
    ]
    result = create_combination(3, operators)
    assert result == expected


def test_is_valid_calibration():
    calibration = {7290: [6, 8, 6, 15]}
    operators = ("+", "*", "||")
    result = is_valid_calibration(calibration, operators)
    assert result == True


def test_solve_part1() -> None:
    assert solve_part1(INPUT_S) == 3749


def test_solve_part2() -> None:
    assert solve_part2(INPUT_S) == 11387


if __name__ == "__main__":
    pytest.main(["-vv", "-s", __file__])
