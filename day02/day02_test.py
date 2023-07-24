from itertools import permutations

from day02 import parse_input, compute_scores, decipher_pair  # type: ignore


INPUT_S: str = """A Y
B X
C Z
"""


def main() -> None:
    msg: str = "TESTING Part1"
    print(f"\n{'=' * len(msg)}")
    print(msg)
    print(f"{'-' * len(msg)}")

    lines: list[str] = parse_input(INPUT_S)
    scores: list[int] = compute_scores(lines)
    part1_score: int = sum(scores)
    print(lines)
    print(scores)
    print(part1_score)

    msg = "TESTING Part2"
    print(f"\n{'=' * len(msg)}")
    print(msg)
    print(f"{'-' * len(msg)}")

    decipherd_pairs: list[str] = [decipher_pair(pair) for pair in lines]
    print(decipherd_pairs)
    deciphered_scores: list[int] = compute_scores(decipherd_pairs)
    part2_score: int = sum(deciphered_scores)
    print(deciphered_scores)
    print(part2_score)
    assert part1_score == 15
    assert part2_score == 12


def generate_rockpaperscissors_model() -> None:
    options: dict[str, int] = {
        "rock": 0,
        "paper": 1,
        "scissors": 2,
    }
    for comb in permutations(options.keys(), 2):
        score: int = (options[comb[0]] - options[comb[1]]) % len(options)
        winner: str = ""
        if score == 0:
            winner = "tie"
        elif score <= 1:
            winner = f"{comb[0]} wins (player 1)"
        elif score > 1:
            winner = f"{comb[1]} wins (player 2)"
        else:
            raise ValueError(f"Unreachable branch: {score=}")
        print(f"{comb}: {score}, {winner}")


if __name__ == "__main__":
    main()
