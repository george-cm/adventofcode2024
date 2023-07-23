import sys
from pathlib import Path
import timeit
from datetime import timedelta

sys.path.append("../")
from input import load_input


INPUT_S: str = load_input(Path("input.txt"))


def get_calories(input_s: str) -> list[int]:

    calories = []

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
    max1 = 0
    max2 = 0
    max3 = 0
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


def main():
    repeats = 10
    number = 100_000
    calories = get_calories(INPUT_S)

    def part1_fortiming():
        return part1(calories)

    part1t = sum(timeit.repeat(part1_fortiming, repeat=repeats, number=number)) / repeats
    part1_v = part1(calories)
    print(f"part1: {part1_v} -  {timedelta(seconds=part1t)}")

    def part2v1_fortiming():
        return part2_v1(calories)

    part2v1t = sum(timeit.repeat(part2v1_fortiming, repeat=repeats, number=number)) / repeats
    part2v1_v = part2_v1(calories)
    print(f"part2_v1: {part2v1_v} -  {timedelta(seconds=part2v1t)}")

    def part2v2_fortiming():
        return part2_v2(calories)

    part2v2t = sum(timeit.repeat(part2v2_fortiming, repeat=repeats, number=number)) / repeats
    part2v2_v = part2_v2(calories)
    print(f"part2_v2: {part2v2_v} -  {timedelta(seconds=part2v2t)}")


if __name__ == "__main__":
    main()
