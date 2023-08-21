from pathlib import Path

from adventofcode2022.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")


def get_calories(input_s: str) -> list[int]:
    calories: list[int] = []

    running_calories = 0
    for line in INPUT_S.splitlines():
        if not line:
            calories.append(running_calories)
            running_calories = 0
        else:
            running_calories += int(line)
    return calories


def part1(calories: list[int]) -> int:
    return max(calories)


def part2_v1(calories: list[int]) -> int:
    max1: int = 0
    max2: int = 0
    max3: int = 0
    for calory in calories:
        if calory > max3:
            max1 = max2
            max2 = max3
            max3 = calory
        elif calory > max2:
            max1 = max2
            max2 = calory
        elif calory > max1:
            max1 = calory
        else:
            pass
    return max1 + max2 + max3


def part2_v2(calories: list[int]) -> int:
    return sum(sorted(calories)[-3:])


def main() -> None:
    calories: list[int] = get_calories(INPUT_S)

    part1_v: int = part1(calories)
    print(f"part1: {part1_v}")

    part2v1_v: int = part2_v1(calories)
    print(f"part2_v1: {part2v1_v}")

    part2v2_v: int = part2_v2(calories)
    print(f"part2_v2: {part2v2_v}")


if __name__ == "__main__":
    main()
