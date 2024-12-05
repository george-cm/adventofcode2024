from pathlib import Path

from adventofcode.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")
# INPUT_S: str = load_input(Path(__file__).parent / "example.txt")


def transpose(lst: list[str]) -> list[str]:
    return [list(x) for x in zip(*lst)]


def part1():
    sum_distances = sum(
        map(
            lambda lst: max(lst) - min(lst),
            transpose(
                map(
                    lambda lst: sorted(lst),
                    transpose(
                        (
                            map(lambda n: int(n), x.split())
                            for x in (line for line in INPUT_S.strip().split("\n"))
                        )
                    ),
                )
            ),
        )
    )
    return sum_distances


def part2():
    tmp = transpose(
        map(lambda n: int(n), x.split()) for x in (line for line in INPUT_S.strip().split("\n"))
    )
    tmp1 = sum(
        map(
            lambda it: it[0] * it[1],
            transpose([tmp[0], list(map(lambda n: tmp[1].count(n), tmp[0]))]),
        )
    )
    return tmp1


def main() -> None:
    part1_v: int = part1()
    print(f"part1: {part1_v}")

    part2v1_v: int = part2()
    print(f"part2_v1: {part2v1_v}")

    part2v2_v: int = 1
    print(f"part2_v2: {part2v2_v}")

    # print(INPUT_S)


if __name__ == "__main__":
    main()
