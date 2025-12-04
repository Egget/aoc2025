#!/usr/bin/env python3


def find_number(n, n_len):
    number = [(-1,-1)]*n_len
    l = len(n)
    for i, k in n:
        min_i = max(0, n_len - (len(n) - i))
        for j in range(min_i, n_len):
            if number[j] == (-1,-1):
                number[j] = (i, k)
                break
            elif number[j][0] > i:
                break
    s_n = 0
    for i, x in number:
        s_n = s_n*10 + x
    return s_n

def sort_batteries(batteries):
    return list(map(lambda x: list(sorted(enumerate((map(int, x))), key=lambda x: (-x[1], x[0]))), batteries))

def part1(data: list[str]) -> int | str:
    ns = sort_batteries(data)
    s = 0
    for n in ns:
        s += find_number(n, 2)
    return s

def part2(data: list[str]) -> int | str:
    ns = sort_batteries(data)
    s = 0
    for n in ns:
        s += find_number(n,12)
    return s

def read_input(filename: str = "input.txt") -> list[str]:
    with open(filename, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    data = read_input(filename)

    print("Advent of Code 2025 - Day 03")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
