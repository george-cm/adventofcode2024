import argparse
from pathlib import Path
from string import Template


def load_input(inputfile: Path) -> str:
    with inputfile.open("r") as inf:
        content: str = inf.read()
    return content


def create_day(day: int) -> None:
    base_path = Path(__file__).parent

    day_file = base_path / "template/day${day}.py"
    new_day_file_name_template = Template(day_file.name)
    day_str = f"{day:02d}"
    new_day_file_name = f"{new_day_file_name_template.substitute(day=day_str)}"
    new_day_fld = base_path.parent.parent / f"day{day_str}"

    if new_day_fld.exists():
        raise OSError("Folder exists: '%s'" % new_day_fld)
    else:
        new_day_fld.mkdir()

    with day_file.open("r", encoding="utf-8") as f:
        new_day_file_content = f.read()

    new_day_file = new_day_fld / new_day_file_name
    with new_day_file.open("w", encoding="utf-8") as f:
        f.write(new_day_file_content)

    day_test_file = base_path / "template/day${day}_test.py"
    new_day_test_file_name_template = Template(day_test_file.name)
    new_day_test_file_name = (
        f"{new_day_test_file_name_template.substitute(day=day_str)}"
    )

    with day_test_file.open("r", encoding="utf-8") as f:
        new_day_test_file_content = f.read()
        new_day_test_file_content = Template(new_day_test_file_content).substitute(
            day=day_str
        )

    new_day_test_file = new_day_fld / new_day_test_file_name
    with new_day_test_file.open("w", encoding="utf-8") as f:
        f.write(new_day_test_file_content)

    new_day_problem_statement_file = new_day_fld / f"problem_day{day_str}.txt"
    new_day_problem_statement_file.write_text("")

    (new_day_fld / "input.txt").write_text("")


def main():
    parser = argparse.ArgumentParser(
        prog="adventofcode2022",
        description="create the files needed to work on a certain Advent of Code problem",
    )
    parser.add_argument(
        "day",
        type=int,
    )
    args = parser.parse_args()
    create_day(args.day)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
