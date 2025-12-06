#!/usr/bin/env python3

def part1(ranges: list[str], ids: list[int]) -> int | str:
    s = []
    for i in ids:
        for l, h in ranges:
            if i >= l and i <= h:
                s.append(i)
                break
    return s

def part1_print(ranges: list[str], ids: list[int]) -> int | str:
    s = []
    for i in ids:
        for l, h in ranges:
            if i >= l and i <= h:
                print(i, l, h)
                s.append(i)
                break
    return s


def part2(ranges: list[tuple[int]], ids) -> int | str:
    ids_that_worked = part1(ranges, ids)
    ranges.sort()
#    print(ranges)
    new_ranges = []
    i = 0
    while i < len(ranges):
        new_l = ranges[i][0]
        max_h = ranges[i][1]
        j = i + 1
        while j < len(ranges) and ranges[j][0] <= max_h:
            max_h = max(ranges[j][1], max_h)
            j += 1
        j -= 1
        new_ranges.append((new_l, max_h))
        i = j + 1
#    print(new_ranges)
    check_these = list(set(ids_that_worked) - set(part1(new_ranges, ids)))
    part1_print(ranges, check_these)
#    print(list(map(lambda x: x[1] - x[0] + 1, new_ranges)))
    return sum(map(lambda x: x[1] - x[0] + 1, new_ranges))


def read_input(filename: str = "input.txt") -> list[str]:
    with open(filename, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    data = read_input(filename)
    ranges = []
    ids = []
    for i, r in enumerate(data):
        if r == '':
            ids = list(map(int, data[i+1:]))
            ranges = list(map(lambda x: tuple(map(int, x.split('-'))), ranges))
            break
        ranges.append(r)

    print("Advent of Code 2025 - Day 05")
    #print("Part 1:", part1(ranges, ids))
    print("Part 2:", part2(ranges, ids))
