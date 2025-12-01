#!/usr/bin/env python3

def part1(data: list[str]) -> int | str:
    def rotate(rotation, n):
        if rotation[0] == 'L':
            n -= int(rotation[1:])
        else:
            n += int(rotation[1:])
        return n % 100
    dial = 50
    s = 0
    for r in data:
        dial = rotate(r, dial)
        if dial == 0:
            s += 1
    return s


def part2(data: list[str]) -> int | str:
    dial = 50
    s = 0
    for r in data:
        if r[0] == 'L':
            new_dial = dial - int(r[1:])
        else:
            new_dial = dial + int(r[1:])
        if new_dial == 0:
            s += 1
        else:
            s += abs(new_dial)//100
            if dial > 0 and new_dial < 0:
                s += 1
        dial = new_dial%100
    return s


def read_input(filename: str = "input.txt") -> list[str]:
    with open(filename, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    data = read_input(filename)

    print("Advent of Code 2025 - Day 01")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
