#!/usr/bin/env python3

from collections import defaultdict

def part1(data: list[str]) -> int | str:
    beams = set()
    splits = 0
    for l in data:
        for i, c in enumerate(l):
            if c == 'S':
                beams.add(i)
            elif c == '^' and i in beams:
                beams.remove(i)
                beams.add(i+1)
                beams.add(i-1)
                splits += 1
    return splits


def part2(data: list[str]) -> int | str:
    beams = defaultdict(int)
    splits = 0
    for l in data:
        for i, c in enumerate(l):
            if c == 'S':
                beams[i] += 1
            elif c == '^' and beams[i] > 0:
                beams[i+1] += beams[i]
                beams[i-1] += beams[i]
                beams[i] = 0
    return sum(beams.values())


def read_input(filename: str = "input.txt") -> list[str]:
    with open(filename, encoding="utf-8") as f:
        return [list(line.rstrip("\n")) for line in f]


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    data = read_input(filename)

    print("Advent of Code 2025 - Day 07")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
