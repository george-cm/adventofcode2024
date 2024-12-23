from collections import defaultdict
from pathlib import Path

from adventofcode.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")


def update_is_valid(update: list[str], rules: dict[str, list[str]]) -> bool:
    is_valid = True
    for i, page in enumerate(update):
        page_rule = rules[page]
        for right_page in update[i+1:]:
            if right_page in page_rule:
                is_valid = False
                return is_valid
    return is_valid


def sum_middle(valid_updates: list[list[str]]) -> int:
    return sum([int(x[len(x)//2]) for x in valid_updates])


def parse_rules_and_updates(inputs: str) -> tuple[dict[str, list[str]], list[list[str]]]:
    rules_str, _, updates_str = inputs.strip().partition("\n\n")
    updates = [x.split(",") for x in updates_str.split("\n")]
    rules = defaultdict(list)
    for rule in rules_str.split("\n"):
        left, right = rule.split("|")
        rules[right].append(left)
    return rules, updates


def fix_update(update: list[str], rules: dict[str, list[str]]) -> list[str]:
    while not update_is_valid(update, rules):
        for i in range(0, len(update)):
            n = update[i]
            rule = rules[n]
            swap = False
            for j in range(i+1, len(update)):
                if update[j] in rule:
                    update[i] = update[j]
                    update[j] = n
                    swap = True
                    break
            if swap:
                break
    return update


def solve_part1(inputs: str) -> int:
    rules, updates = parse_rules_and_updates(inputs)
    valid_updates = [update for update in updates if update_is_valid(update, rules)]
    return sum_middle(valid_updates)


def solve_part2(inputs: str) -> int:
    rules, updates = parse_rules_and_updates(inputs)
    fixed_updates = [fix_update(update, rules)
                     for update in updates if not update_is_valid(update, rules)]
    return sum_middle(fixed_updates)


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
