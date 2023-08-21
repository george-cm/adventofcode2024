from pathlib import Path
from typing import NamedTuple

from adventofcode2022.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")


class Instruction(NamedTuple):
    move: int
    from_stack: int
    to_stack: int


def parse_input(inputs: str) -> tuple[list[list[str]], list[Instruction]]:
    lines: list[str] = inputs.splitlines()
    stacks: list[list[str]] = []
    instructions: list[namedtuple["move", "from", "to"]] = []
    passed_stacks: bool = False
    stack_count: int = 0
    for line in lines:
        # breakpoint()
        if line.strip() == "":
            passed_stacks = True
        else:
            if not passed_stacks:
                if stack_count == 0:
                    stack_count = (len(line) + 1) // 4
                    for s in range(stack_count):
                        stacks.append(list())
                for i in range(1, len(line) + 1, 4):
                    if line[i].strip() != "":
                        stacks[(i - 1) // 4].append(line[i])
            else:
                parts = line.split(" ")
                move = int(parts[1])
                from_stack = int(parts[3])
                to_stack = int(parts[5])
                instructions.append(Instruction(move, from_stack, to_stack))
    stacks = [list(reversed(s[:-1])) for s in stacks]
    return stacks, instructions


def execute_instruction_part1(
    instruction: Instruction, stacks: list[list[str]]
) -> None:
    for _ in range(instruction.move):
        crate = stacks[instruction.from_stack - 1].pop()
        stacks[instruction.to_stack - 1].append(crate)


def execute_instruction_part2(
    instruction: Instruction, stacks: list[list[str]]
) -> None:
    crates = stacks[instruction.from_stack - 1][-instruction.move :]
    stacks[instruction.from_stack - 1] = stacks[instruction.from_stack - 1][
        : -instruction.move
    ]
    stacks[instruction.to_stack - 1].extend(crates)


def solve_part1(inputs: str) -> int:
    result: str = ""
    # write code here, update rusult
    stacks, instructions = parse_input(inputs)
    for instruction in instructions:
        execute_instruction_part1(instruction, stacks)
    for stack in stacks:
        result += stack[-1]
    return result


def solve_part2(inputs: str) -> int:
    result: str = ""
    # write code here, update rusult
    stacks, instructions = parse_input(inputs)
    for instruction in instructions:
        execute_instruction_part2(instruction, stacks)
    for stack in stacks:
        result += stack[-1]
    return result


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
