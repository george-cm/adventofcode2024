from pathlib import Path

from adventofcode2022.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")


def create_path(dir_stack: list[str]) -> str:
    return "/".join(dir_stack).replace("//", "/")


def compute_dir_size(dir_contents: dict[str, dict[str, int]], dirname: str) -> int:
    return sum(
        (
            sum(files_dict.values())
            for dir_path, files_dict in dir_contents.items()
            if dir_path.startswith(dirname)
        )
    )


def solve_part1(inputs: str) -> int:
    result: int = 0
    # write code here, update rusult
    dir_stack: list[str] = []
    # directory_stack.append(current_dir)
    directory_contents: dict[str, dict[str, int]] = {}
    lines = inputs.splitlines()
    for line in lines:
        match line.split(" "):
            case ("$", "cd", ".."):
                if dir_stack:
                    dir_stack.pop()
                current_dir_path = create_path(dir_stack)

            case ("$", "cd", location):
                dir_stack.append(location)
                current_dir_path = create_path(dir_stack)

            case ("$", "ls"):
                pass

            case ("dir", dirname):
                current_dir_path = create_path(dir_stack)
                dir_path = f"{current_dir_path}/{dirname}".replace("//", "/")
                if dir_path not in directory_contents:
                    directory_contents[dir_path] = {}

            case (filesize_str, filename):
                current_dir_path = create_path(dir_stack)
                filesize = int(filesize_str)
                if current_dir_path not in directory_contents:
                    directory_contents[current_dir_path] = {}
                directory_contents[current_dir_path][filename] = filesize

    for dir_path in directory_contents:
        dir_size = compute_dir_size(directory_contents, dir_path)
        if dir_size <= 100_000:
            result += dir_size

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
