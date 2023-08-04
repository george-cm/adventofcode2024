from pathlib import Path


def load_input(inputfile: Path) -> str:
    with inputfile.open("r") as inf:
        content: str = inf.read()
    return content


def create_day(day: int) -> None:
    # TODO: implement this function to create the files for a new day based on the template.
    ...


if __name__ == "__main__":
    ...
