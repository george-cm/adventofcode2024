from functools import cache
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


@cache
def create_combination(
    num_operators: int, operators: tuple[str, ...]
) -> list[list[str]]:
    if num_operators == 0:
        return []
    accumulator = []
    for operator in operators:
        next_combinations = create_combination(num_operators - 1, operators)
        if next_combinations:
            for combination in next_combinations:
                accumulator.append([operator] + combination)
        else:
            accumulator.append([operator])
    return accumulator


def is_valid_calibration(
    calibration: dict[int, list[int]], operators: tuple[str, ...]
) -> bool:
    test_value = list(calibration.keys())[0]
    operands = list(calibration.values())[0]
    operator_combinations = create_combination(len(operands) - 1, operators)
    for operator_combination in operator_combinations:
        acc = operands[0]
        for i, operator in enumerate(operator_combination):
            match operator:
                case "+":
                    acc += operands[i + 1]
                case "*":
                    acc *= operands[i + 1]
                case "||":
                    acc = int(str(acc) + str(operands[i + 1]))
            if acc > test_value:
                # print(
                #     f"{test_value=} | {acc=} | {operands=} | {operator_combination=}"
                # )
                break
        if acc == test_value:
            return True
    return False


def solve_part1(inputs: str) -> int:
    operators = ("+", "*")
    calibrations = parse_input(inputs)
    valid_test_values: list[int] = []
    for calibration in calibrations:
        if is_valid_calibration(calibration, operators):
            valid_test_values.append(list(calibration.keys())[0])
    result: int = sum(valid_test_values)
    return result


def solve_part2(inputs: str) -> int:
    operators = ("+", "*", "||")
    calibrations = parse_input(inputs)
    valid_test_values: list[int] = []
    for calibration in calibrations:
        if is_valid_calibration(calibration, operators):
            valid_test_values.append(list(calibration.keys())[0])
    result: int = sum(valid_test_values)
    return result


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
