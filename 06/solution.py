#!/usr/bin/env python3

import re
from operator import mul
from functools import reduce

def part1(data: list[str]) -> int | str:
    data = list(map(lambda x: list(filter(lambda y: y != '', re.split(r'\s+', x))), data))
    transposed = []
    for i in range(len(data[0])):
        new_l = []
        for l in data:
            new_l.append(l[i])
        transposed.append(new_l)
    s = 0
    for p in transposed:
        if p[-1] == '*':
            s += reduce(mul, map(int, p[:-1]), 1)
        else:
            s += sum(map(int, p[:-1]))
    return s


def part2(data: list[str]) -> int | str:
    problems = []
    ops = list(filter(lambda x: x != '', re.split(r'\s+', data[-1])))
    s = 0
    n_ns = len(data) - 1
    problem = []
    for i in range(len(data[0])):
        number = ''
        for l in data[:-1]:
            number += l[i]
        if len(number.replace(' ', '')) == 0:
            problems.append(problem)
            problem = []
        else:
            n = 0
            for d in number:
                if d != ' ':
                    n = 10*n + int(d)
            problem.append(n)
    problems.append(problem)
    for o, p in enumerate(problems):
        if ops[o] == '*':
            s += reduce(mul, p, 1)
        else:
            s += sum(p)
    return s

def read_input(filename: str = "input.txt") -> list[str]:
    with open(filename, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    data = read_input(filename)
    print("Advent of Code 2025 - Day 06")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
