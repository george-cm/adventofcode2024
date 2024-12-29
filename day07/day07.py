from pathlib import Path

from adventofcode.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")


def parse_input(input_str: str) -> list[dict[int, list[int]]]:
    """
    Args:
    input_str: str of the form
        test_value1: num1 num2 ...
        test_value2: num1 num2 ...
        ...

    Returns:
    list[dict[int, list[int]]]
        [{test_value1: [num1, num2, ...]},
        {test_value1: [num1, num2, ...]}, ...]
    """
    return [
        {
            int(line.strip().split(":")[0]): [
                int(x) for x in line.strip().split(":")[1].strip().split(" ")
            ]
        }
        for line in input_str.strip().split("\n")
    ]


def is_valid_calibration(
    calibration: dict[int, list[int]], operators: list[str]
) -> bool:
    test_value = list(calibration.keys())[0]
    operands = list(calibration.values())[0]
    print(test_value)
    print(operands)


def solve_part1(inputs: str) -> int:
    operators = ["+", "*"]
    calibrations = parse_input(inputs)
    valid_test_values: list[int] = []
    for calibration in calibrations:
        if is_valid_calibration(calibration, operators):
            valid_test_values.append(calibration.keys()[0])
    result: int = 0
    # write code here, update rusult

    return result


def solve_part2(inputs: str) -> int:
    result: int = 0
    # write code here, update rusult

    return result


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
