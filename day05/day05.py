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
    instructions: list[Instruction] = []
    passed_stacks: bool = False
    stack_count: int = 0
    for line in lines:
        if not passed_stacks and line.strip():
            if stack_count == 0:
                stack_count = (len(line) + 1) // 4
                stacks.extend([] for _ in range(stack_count))
            for i in range(1, len(line) + 1, 4):
                if line[i].strip() != "":
                    stacks[(i - 1) // 4].append(line[i])
        elif passed_stacks:
            parts = line.split(" ")
            move = int(parts[1])
            from_stack = int(parts[3]) - 1
            to_stack = int(parts[5]) - 1
            instructions.append(Instruction(move, from_stack, to_stack))
        else:
            passed_stacks = True
    stacks = [list(reversed(s[:-1])) for s in stacks]
    return stacks, instructions


def execute_instruction_part1(
    instruction: Instruction, stacks: list[list[str]]
) -> None:
    for _ in range(instruction.move):
        crate = stacks[instruction.from_stack].pop()
        stacks[instruction.to_stack].append(crate)


def execute_instruction_part2(
    instruction: Instruction, stacks: list[list[str]]
) -> None:
    crates = stacks[instruction.from_stack][-instruction.move :]
    stacks[instruction.from_stack] = stacks[instruction.from_stack][: -instruction.move]
    stacks[instruction.to_stack].extend(crates)


def solve_part1(inputs: str) -> str:
    stacks, instructions = parse_input(inputs)
    for instruction in instructions:
        execute_instruction_part1(instruction, stacks)
    return "".join([stack[-1] for stack in stacks])


def solve_part2(inputs: str) -> str:
    stacks, instructions = parse_input(inputs)
    for instruction in instructions:
        execute_instruction_part2(instruction, stacks)
    return "".join([stack[-1] for stack in stacks])


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
