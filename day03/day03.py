import re
from pathlib import Path

from adventofcode.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input1.txt")
# INPUT_S: str = load_input(Path(__file__).parent / "example.txt")
# print(INPUT_S)


def parse_int_tup(int_tup: tuple[str, str]) -> tuple[int, int]:
    return int(int_tup[0]), int(int_tup[1])


def solve_part1(inputs: str) -> int:
    reformatted = inputs.replace(")", ")\n").split("\n")
    patt = re.compile(r"mul\((\d+?),(\d+?)\)")
    result = sum(y[0] * y[1] for y in
                 ((lambda x: parse_int_tup(patt.findall(x)[0]) if patt.findall(x) else None)(x)
                  for x in reformatted if patt.search(x)))
    return result


def solve_part2(inputs: str) -> int:
    calculation_enabled = True
    sum_total = 0
    reformatted = inputs.replace(")", ")\n").split("\n")
    patt = re.compile(r"mul\((\d+?),(\d+?)\)")
    for line in reformatted:
        if "don't()" in line:
            calculation_enabled = False
        elif "do()" in line:
            calculation_enabled = True
        if x := patt.findall(line):
            if calculation_enabled:
                y = parse_int_tup(x[0])
                sum_total += (y[0] * y[1])
    return sum_total


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
