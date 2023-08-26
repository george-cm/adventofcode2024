import sys

import pytest

from day06 import solve_part1, solve_part2  # type: ignore  # noqa", 402),

INPUT_S: str = """"""


@pytest.mark.parametrize(
    ("input_stream", "first_marker_position"),
    (
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ),
)
def test_solve_part1(input_stream, first_marker_position) -> None:
    assert solve_part1(input_stream) == first_marker_position


@pytest.mark.parametrize(
    ("input_stream", "first_marker_position"),
    (
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ),
)
def test_solve_part2(input_stream, first_marker_position) -> None:
    assert solve_part2(input_stream) == first_marker_position


if __name__ == "__main__":
    pytest.main(["-vv", "-s", __file__])
