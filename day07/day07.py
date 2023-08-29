from pathlib import Path
from typing import TypedDict

from adventofcode2022.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")


class FSEntry(TypedDict):
    dirsize: int
    contents: dict[str, int]


def create_path(dir_stack: list[str]) -> str:
    return "/".join(dir_stack).replace("//", "/")


def compute_dir_size(filesystem: dict[str, FSEntry], dirname: str) -> int:
    return sum(
        (
            sum(files_dict["contents"].values())
            for dir_path, files_dict in filesystem.items()
            if dir_path.startswith(dirname)
        )
    )


def update_dir_sizes(
    filesystem: dict[str, FSEntry], current_dir_path: str, filesize: int
) -> None:
    if current_dir_path == "/":
        return
    dir_stack: list[str] = current_dir_path.split("/")
    dir_stack[0] = "/"
    dir_path: str = ""
    dir_stack.pop()
    while dir_stack:
        dir_path = create_path(dir_stack)
        filesystem[dir_path]["dirsize"] += filesize
        dir_stack.pop()


def create_filesystem(inputs: str) -> dict[str, FSEntry]:
    dir_stack: list[str] = []
    # directory_stack.append(current_dir)
    filesystem: dict[str, FSEntry] = {}
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
                if dir_path not in filesystem:
                    filesystem[dir_path] = {"dirsize": 0, "contents": {}}

            case (filesize_str, filename):
                current_dir_path = create_path(dir_stack)
                filesize = int(filesize_str)
                if current_dir_path not in filesystem:
                    filesystem[current_dir_path] = {"dirsize": 0, "contents": {}}
                filesystem[current_dir_path]["contents"][filename] = filesize
                filesystem[current_dir_path]["dirsize"] += filesize
                update_dir_sizes(filesystem, current_dir_path, filesize)

    return filesystem


def solve_part1(inputs: str) -> int:
    result: int = 0
    # write code here, update rusult
    filesystem = create_filesystem(inputs)
    for dir_path in filesystem:
        dir_size = filesystem[dir_path]["dirsize"]
        if dir_size <= 100_000:
            result += dir_size

    return result


def solve_part2(inputs: str) -> int:
    # write code here, update rusult
    filesystem = create_filesystem(inputs)
    total_disk_space: int = 70_000_000
    needed_unused_space: int = 30_000_000
    free_space: int = total_disk_space - filesystem["/"]["dirsize"]
    min_space_to_free: int = needed_unused_space - free_space
    dir_to_delete: str = ""
    size_of_dir_to_delete: int = 0
    for dir_path in filesystem:
        if not dir_to_delete and filesystem[dir_path]["dirsize"] >= min_space_to_free:
            dir_to_delete = dir_path
            size_of_dir_to_delete = filesystem[dir_to_delete]["dirsize"]
        else:
            size_of_dir_path = filesystem[dir_path]["dirsize"]
            if (
                size_of_dir_path >= min_space_to_free
                and size_of_dir_path < size_of_dir_to_delete
            ):
                dir_to_delete = dir_path
                size_of_dir_to_delete = size_of_dir_path

    return size_of_dir_to_delete


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
