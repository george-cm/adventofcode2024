from pathlib import Path


def load_input(inputfile: Path) -> str:
    with inputfile.open("r") as inf:
        content: str = inf.read()
    return content


if __name__ == "__main__":
    ...
