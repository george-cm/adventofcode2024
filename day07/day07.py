from pathlib import Path

from adventofcode2022.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")


def get_dir(tree: dict,
            dir_name: str,
            parent: str | None = None) -> tuple[dict | None, str | None]:
    for k, v in tree:
        if k == dir_name:
            return v, parent
        elif isinstance(v, dict):
            return get_dir(v, dir_name, k)
    return None, None


def solve_part1(inputs: str) -> int:
    result: int = 0
    # write code here, update rusult
    directory_stack: list[str] = []
    current_dir: str = "/"
    directory_stack.append(current_dir)
    lines = inputs.splitlines()
    for line in lines:
        match line.split(" "):
            case ("$", "cd", ".."):
                if len(directory_stack) >= 2:
                    directory_stack.pop()
                    current_dir = directory_stack[-1]
                print(
                    f"changing directory back up one level to {current_dir=}")
            case ("$", "cd", location):
                directory_stack.append(location)
                current_dir = location
                print(f"changing directory to {location=}")
            case ("$", "ls"):
                print("listing...")
            case ("dir", dirname):
                print(f"{dirname=}")
            case (filesize, filename):
                print(f"{filename=} => {filesize=}")
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
