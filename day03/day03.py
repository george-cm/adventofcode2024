import sys
from pathlib import Path

sys.path.append("../")
from input import load_input


INPUT_S: str = load_input(Path("input.txt"))

ELF_CHOICES: str = "ABC"
HUMAN_CHOICES: str = "XYZ"
assert len(ELF_CHOICES) == len(HUMAN_CHOICES)
OPTIONS_COUNT: int = len(ELF_CHOICES)
THRESHOLD: int = OPTIONS_COUNT // 2


def decipher_pair(pair: str) -> str:
    # for part 2
    player1_choice: int = ELF_CHOICES.index(pair[0])
    player2_choice: int = 0
    match pair[1]:
        case "X":
            player2_choice = player1_choice - (THRESHOLD // (1 - ((1 // OPTIONS_COUNT) * OPTIONS_COUNT)))
        case "Y":
            player2_choice = player1_choice
        case "Z":
            player2_choice = player1_choice - (THRESHOLD // (1 - ((1 // OPTIONS_COUNT) * OPTIONS_COUNT))) - 1
    assert player2_choice < OPTIONS_COUNT
    return f"{pair[0]}{HUMAN_CHOICES[player2_choice]}"


def parse_input(inputs: str) -> list[str]:
    lines: list[str] = inputs.splitlines()
    pairs: list[str] = [x.strip().replace(" ", "") for x in lines]
    for x in pairs:
        assert len(x) == 2
        assert x[0] in ELF_CHOICES
        assert x[1] in HUMAN_CHOICES
    return pairs


def who_wins(game: str) -> int:
    """returns 0 for tie, 1 for player 1, 2 for player 2"""
    player1_choice: int = ELF_CHOICES.index(game[0])
    player2_choice: int = HUMAN_CHOICES.index(game[1])
    score: int = (player1_choice - player2_choice) % OPTIONS_COUNT
    if score == 0:
        return 0
    if score <= THRESHOLD:
        return 1
    if score > THRESHOLD and score < OPTIONS_COUNT:
        return 2
    raise ValueError(f"Unreachable branch: {score=}")


def compute_scores(pairs: list[str]) -> list[int]:
    points: list[int] = []
    for pair in pairs:
        tmp_points: int = 0
        human_choice = HUMAN_CHOICES.index(pair[1])
        match human_choice:
            case 0:
                tmp_points += 1
            case 1:
                tmp_points += 2
            case 2:
                tmp_points += 3
            case _:
                raise ValueError(f"Unreachable branch: {human_choice=}")
        who_won: int = who_wins(pair)
        match who_won:
            case 0:
                tmp_points += 3
            case 1:
                tmp_points += 0
            case 2:
                tmp_points += 6
            case _:
                raise ValueError(f"Unreachable branch: {who_won=}")
        points.append(tmp_points)
    return points


def main() -> None:
    lines: list[str] = parse_input(INPUT_S)
    scores: list[int] = compute_scores(lines)
    total_score: int = sum(scores)
    print(f"Part1: total_score = \n{total_score}")
    deciphered_scores: list[str] = [decipher_pair(pair) for pair in lines]
    part2_scores: list[int] = compute_scores(deciphered_scores)
    part2_total_score: int = sum(part2_scores)
    print(f"Part2: total_score = \n{part2_total_score}")


if __name__ == "__main__":
    main()
