from pathlib import Path

from adventofcode2022.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")


def solve_part1(inputs: str) -> int:
    lines = inputs.splitlines()
    total_priority: int = 0
    for line in lines:
        setleft: set[str] = set(line[: len(line) // 2])
        setright: set[str] = set(line[len(line) // 2 :])
        common_item: set[str] = setleft.intersection(setright)
        if common_item is not None:
            priority: int = calculate_priority(tuple(common_item)[0])
            total_priority += priority

    return total_priority


def solve_part2(inputs: str) -> int:
    lines: list[str] = inputs.splitlines()
    total_priority: int = 0
    for group in (lines[i : i + 3] for i in range(0, len(lines), 3)):
        set_1: set[str] = set(group[0])
        set_2: set[str] = set(group[1])
        set_3: set[str] = set(group[2])
        item: str = list(set_1.intersection(set_2).intersection(set_3))[0]
        total_priority += calculate_priority(item)
    return total_priority


def calculate_priority(c: str) -> int:
    result: int = ord(c) - ord("A") + 27 if c < "a" else ord(c) - ord("a") + 1
    return result


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
