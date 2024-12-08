from pathlib import Path
# from pprint import pprint as print


from adventofcode.common import load_input

# INPUT_S: str = load_input(Path(__file__).parent / "input.txt")
INPUT_S: str = load_input(Path(__file__).parent / "example.txt")


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


def part1() -> int:
    reports = [
        [int(level) for level in line.split()]
        for line in INPUT_S.strip().split("\n")
    ]
    return sum(map(lambda report: is_safe(1, 3, report), reports))


def main() -> None:
    print(f"Part1: {part1()}")


if __name__ == "__main__":
    main()
