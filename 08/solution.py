#!/usr/bin/env python3

from math import sqrt
import heapq


def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

def build_circuits_dict(data):
    circuits = dict()
    for p in data:
        circuits[p] = set([p])
    return circuits

def build_distance_heap(data):
    distances = []
    for i, p1 in enumerate(data):
        for p2 in data[i+1:]:
            heapq.heappush(distances, (distance(p1, p2), p1, p2))
    return distances

def part1(data: list[str], connections: int) -> int | str:
    distances = build_distance_heap(data)
    circuits = build_circuits_dict(data)
    i = 0
    while i < connections:
        (d, p1, p2) = heapq.heappop(distances)
        new_set = circuits[p1] | circuits[p2]
        for p in new_set:
            circuits[p] = new_set
        i += 1
    s = 0
    visited = set()
    c_lens = []
    for p, c in circuits.items():
        if p in visited:
            continue
        visited |= c
        heapq.heappush(c_lens, -len(c))
    return abs(heapq.heappop(c_lens) * heapq.heappop(c_lens) * heapq.heappop(c_lens))


def part2(data: list[str]) -> int | str:
    distances = build_distance_heap(data)
    circuits = build_circuits_dict(data)
    target = len(data)
    i = 0
    while True:
        (d, p1, p2) = heapq.heappop(distances)
        new_set = circuits[p1] | circuits[p2]
        if len(new_set) == target:
            return p1[0]*p2[0]
        for p in new_set:
            circuits[p] = new_set
        i += 1

def read_input(filename: str = "input.txt") -> list[str]:
    with open(filename, encoding="utf-8") as f:
        return [tuple(map(int, line.rstrip("\n").split(','))) for line in f]


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    connections = 10 if len(sys.argv) > 1 and sys.argv[1] == 'test.txt' else 1000
    data = read_input(filename)

    print("Advent of Code 2025 - Day 08")
    print("Part 1:", part1(data, connections))
    print("Part 2:", part2(data))
