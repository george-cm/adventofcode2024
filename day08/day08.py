from collections import defaultdict
from pathlib import Path
from typing import TypeAlias

from adventofcode.common import load_input

INPUT_S: str = load_input(Path(__file__).parent / "input.txt")

Grid: TypeAlias = list[list[str]]
Location: TypeAlias = tuple[int, int]
Locations: TypeAlias = list[Location]
SetLocations: TypeAlias = set[Location]
AntennaeLocations: TypeAlias = dict[str, Locations]
LocationPair: TypeAlias = tuple[Location, Location]
LocationPairs: TypeAlias = list[LocationPair]


def create_grid(inputs: str) -> list[list[str]]:
    return [list(line) for line in inputs.strip().split("\n")]


def find_antennae(grid: Grid) -> AntennaeLocations:
    antennae: dict[str, list[tuple[int, int]]] = defaultdict(list)
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c != ".":
                antennae[c].append((x, y))
    return antennae


def create_pairs(locations: Locations) -> LocationPairs:
    assert len(locations) >= 2
    if len(locations) == 2:
        sorted_locations = sorted(locations)
        return [(sorted_locations[0], sorted_locations[1])]
    pairs: LocationPairs = []
    first_location: Location = locations[0]
    for loc in locations[1:]:
        sorted_locations = sorted([first_location, loc])
        pairs.append((sorted_locations[0], sorted_locations[1]))
    return pairs + create_pairs(locations[1:])


def find_antennae_pair_antinodes(
    antennae_pair: LocationPair, grid_width: int, grid_height: int
) -> SetLocations:
    antinodes_locations: SetLocations = set()
    antenna1, antenna2 = antennae_pair
    dx: int = antenna1[0] - antenna2[0]
    dy: int = antenna1[1] - antenna2[1]
    antinode1x = antenna1[0] + dx
    antinode1y = antenna1[1] + dy
    if 0 <= antinode1x < grid_width and 0 <= antinode1y < grid_height:
        antinodes_locations.add((antinode1x, antinode1y))

    antinode2x = antenna2[0] - dx
    antinode2y = antenna2[1] - dy
    if 0 <= antinode2x < grid_width and 0 <= antinode2y < grid_height:
        antinodes_locations.add((antinode2x, antinode2y))
    return antinodes_locations


def find_antinodes(
    antennae: AntennaeLocations, grid_width: int, grid_height: int
) -> list[tuple[int, int]]:
    antinodes: SetLocations = set()
    for antenna, locations in antennae.items():
        antenna_pairs = create_pairs(locations)
        for pair in antenna_pairs:
            pair_antinodes = find_antennae_pair_antinodes(
                pair, grid_width, grid_height
            )
            antinodes.update(pair_antinodes)
    return list(antinodes)


def find_antennae_resonant_antinodes(
    antennae_pair: LocationPair, grid_width: int, grid_height: int
) -> SetLocations:
    antinodes_locations: SetLocations = set()
    antenna1, antenna2 = antennae_pair
    antinodes_locations.update([antenna1, antenna2])
    dx: int = antenna1[0] - antenna2[0]
    dy: int = antenna1[1] - antenna2[1]
    in_bounds: bool = True
    i: int = 1
    while in_bounds:
        x = antenna1[0] + i * dx
        y = antenna1[1] + i * dy
        if 0 <= x < grid_width and 0 <= y < grid_height:
            antinodes_locations.add((x, y))
        else:
            in_bounds = False
        i += 1
    i = 1
    in_bounds = True
    while in_bounds:
        x = antenna2[0] - i * dx
        y = antenna2[1] - i * dy
        if 0 <= x < grid_width and 0 <= y < grid_height:
            antinodes_locations.add((x, y))
        else:
            in_bounds = False
        i += 1
    return antinodes_locations


def find_antinodes_w_resonance(
    antennae: AntennaeLocations, grid_width: int, grid_height: int
) -> Locations:
    antinodes: SetLocations = set()
    for antenna, locations in antennae.items():
        antenna_pairs = create_pairs(locations)
        for pair in antenna_pairs:
            pair_antinodes = find_antennae_resonant_antinodes(
                pair, grid_width, grid_height
            )
            antinodes.update(pair_antinodes)
    return list(antinodes)


def display_antinodes(grid: Grid, antinodes_locations: Locations) -> None:
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) in antinodes_locations:
                print("#", end="")
            else:
                print(grid[y][x], end="")
        print()


def solve_part1(inputs: str) -> int:
    grid = create_grid(inputs)
    antennae_locations: AntennaeLocations = find_antennae(grid)
    antinodes_locations: Locations = find_antinodes(
        antennae_locations, len(grid[0]), len(grid)
    )
    # display_antinodes(grid, antinodes_locations)
    return len(antinodes_locations)


def solve_part2(inputs: str) -> int:
    grid = create_grid(inputs)
    antennae_locations: AntennaeLocations = find_antennae(grid)
    antinodes_locations: Locations = find_antinodes_w_resonance(
        antennae_locations, len(grid[0]), len(grid)
    )
    # display_antinodes(grid, antinodes_locations)
    return len(antinodes_locations)


def main() -> None:
    print(f"Part 1 solution: {solve_part1(INPUT_S)}")
    print(f"Part 2 solution: {solve_part2(INPUT_S)}")


if __name__ == "__main__":
    main()
