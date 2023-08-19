from pathlib import Path
from tkinter import W
from typing import Generator

from adventofcode2022.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")


def create_pairs(inputs: str) -> Generator[tuple[tuple[int, int], ...], None, None]:
    lines: list[str] = inputs.splitlines()
    range_pairs_str: Generator[tuple[str, ...], None, None] = (
        tuple(pair.split(",")) for pair in lines
    )
    range_pairs_str2: Generator[tuple[list[str], list[str]], None, None] = (
        (pair[0].split("-"), pair[1].split("-")) for pair in range_pairs_str
    )
    range_pairs: Generator[tuple[tuple[int, int], ...], None, None] = (
        tuple(((int(x[0]), int(x[1])), (int(y[0]), int(y[1]))))
        for x, y in range_pairs_str2
    )
    return range_pairs


def solve_part1(inputs: str) -> int:
    result: int = 0
    # write code here, update rusult
    range_pairs: Generator[tuple[tuple[int, int], ...], None, None] = create_pairs(
        inputs
    )

    for r1, r2 in range_pairs:
        if r1[0] in range(r2[0], r2[1] + 1) and r1[1] in range(r2[0], r2[1] + 1):
            result += 1
        elif r2[0] in range(r1[0], r1[1] + 1) and r2[1] in range(r1[0], r1[1] + 1):
            result += 1
    return result


def solve_part2(inputs: str) -> int:
    result: int = 0
    # write code here, update rusult
    range_pairs: Generator[tuple[tuple[int, int], ...], None, None] = create_pairs(
        inputs
    )

    for r1, r2 in range_pairs:
        if r1[0] in range(r2[0], r2[1] + 1) or r1[1] in range(r2[0], r2[1] + 1):
            result += 1
        elif r2[0] in range(r1[0], r1[1] + 1) or r2[1] in range(r1[0], r1[1] + 1):
            result += 1

    return result


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
