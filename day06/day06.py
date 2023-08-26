from itertools import islice
from pathlib import Path

from adventofcode2022.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")


def get_marker(inputs: str, marker_length: int) -> int:
    for i in range(0, len(inputs) - marker_length):
        if len(set(islice(inputs, i, i + marker_length))) == marker_length:
            return i + marker_length
    raise IOError("Reached and of stream and marker was not found")


def solve_part1(inputs: str) -> int:
    result: int = 0
    # write code here, update rusult
    return get_marker(inputs, 4)


def solve_part2(inputs: str) -> int:
    result: int = 0
    # write code here, update rusult
    return get_marker(inputs, 14)


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
