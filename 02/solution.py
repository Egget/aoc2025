#!/usr/bin/env python3

from itertools import combinations

def part1(data: list[str]) -> int | str:
    def is_invalid(i):
        s = str(i)
        if len(s) % 2 == 0:
            return s[:len(s)//2] == s[len(s)//2:]

    ranges = list(map(lambda x: list(map(int, x.split('-'))), data[0].split(",")))
    s = 0
    for r in ranges:
        for i in range(r[0], r[1]+1):
            if is_invalid(i):
                print(i)
                s += i
    return s

def get_invalids_for_len(l, lower, upper):
    invalids = []
    lower_str = str(lower)
    upper_str = str(upper)
    for p in range(1,l//2+1):
        if l%p != 0: continue
        for i in range(int(lower_str[:p]), int(upper_str[:p]) + 1):
            n = i
            while len(str(n)) < l:
                n = ((10**p)*n) + i
            if n >= lower and n <= upper:
                invalids.append(n)
    return sum(set(invalids))

def get_invalids(r):
    invalids = 0
    min_len = len(str(r[0]))
    max_len = len(str(r[1]))
    for l in range(min_len,max_len+1):
        invalids += get_invalids_for_len(l, max(r[0], 10**(l-1)), min(r[1], 10**l -1))
    return invalids


def part2(data: list[str]) -> int | str:

    ranges = list(map(lambda x: list(map(int, x.split('-'))), data[0].split(",")))
    s = 0
    for r in ranges:
        s += get_invalids(r)
    return s


def read_input(filename: str = "input.txt") -> list[str]:
    with open(filename, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    data = read_input(filename)

    print("Advent of Code 2025 - Day 02")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
