#!/usr/bin/env python3

directions = [(1,0),(-1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,1),(-1,-1)]

def n_adjacent(grid, i, j):
    n = 0
    for di,dj in directions:
        if 0 <= i+di and i+di < len(grid) and 0 <= j+dj and j+dj < len(grid[0]) and grid[i+di][j+dj] == '@':
            n += 1
    return n

def part1(grid: list[str]) -> int | str:
    s = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@' and n_adjacent(grid, i, j) < 4:
                s += 1
    return s


def part2(grid: list[str]) -> int | str:
    s = 0
    for i in range(len(grid)):
        grid[i] = list(grid[i])
    while(True):
        removed = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@' and n_adjacent(grid, i, j) < 4:
                    grid[i][j] = 'x'
                    removed = True
                    s += 1
        if not removed:
            break
    return s


def read_input(filename: str = "input.txt") -> list[str]:
    with open(filename, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    data = read_input(filename)

    print("Advent of Code 2025 - Day 04")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
