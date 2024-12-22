from pathlib import Path
from typing import Generator

# from pprint import pprint as print
from adventofcode.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")
# INPUT_S: str = load_input(Path(__file__).parent / "example.txt")


def is_monotone(lst: list[int]) -> bool:
    deltas = [lst[i] - lst[i - 1] for i in range(1, len(lst))]
    return all(map(lambda n: n > 0, deltas)) or all(
        map(lambda n: n < 0, deltas)
    )


def is_within_limits(lower: int, upper: int, lst: list[int]) -> bool:
    deltas = [lst[i] - lst[i - 1] for i in range(1, len(lst))]
    return all(map(lambda n: lower <= abs(n) <= upper, deltas))


def is_safe(lower: int, upper: int, lst: list[int]) -> bool:
    return is_monotone(lst) and is_within_limits(lower, upper, lst)


def dampen_report(lst: list[int]) -> Generator[list[int], None, None]:
    for i in range(len(lst)):
        yield lst[:i] + lst[i + 1:]


def solve_part1(input_s: str) -> int:
    reports = [
        [int(level) for level in line.split()]
        for line in input_s.strip().split("\n")
    ]
    return sum(map(lambda report: is_safe(1, 3, report), reports))


def solve_part2(input_s: str) -> int:
    reports = [
        [int(level) for level in line.split()]
        for line in input_s.strip().split("\n")
    ]
    return sum(
        map(
            lambda report: is_safe(1, 3, report)
            or any(
                (is_safe(1, 3, dampened) for dampened in dampen_report(report))
            ),
            reports,
        )
    )


def main() -> None:
    print(f"Part1: {solve_part1(INPUT_S)}")
    print(f"Part2: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
