#!/usr/bin/env python3
import argparse
import datetime as dt
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("This script requires the 'requests' package. Install with:")
    print("  pip install requests")
    sys.exit(1)


def get_session_token(env_var: str = "AOC_SESSION") -> str:
    token = os.environ.get(env_var)
    if not token:
        print(
            f"Error: Advent of Code session token not found in environment variable {env_var}.\n"
            "1. Log in to adventofcode.com in your browser.\n"
            "2. Grab the 'session' cookie value.\n"
            f"3. Set it in your shell, e.g.:\n"
            f"   export {env_var}=<your_session_cookie>\n"
        )
        sys.exit(1)
    return token


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Prepare Advent of Code directory, download input, and create "
            "test.txt, solution.py, and run script."
        )
    )
    parser.add_argument(
        "--year",
        type=int,
        help="AOC year (default: current year or $AOC_YEAR if set).",
    )
    parser.add_argument(
        "--day",
        type=int,
        help="Day of month (1–25). If omitted, uses today's day of month.",
    )
    parser.add_argument(
        "--base-dir",
        type=str,
        default=".",
        help="Base directory where the day-folder (01, 02, ...) should be created. Default: current directory.",
    )
    parser.add_argument(
        "--session-env",
        type=str,
        default="AOC_SESSION",
        help="Environment variable name holding your AoC session token. Default: AOC_SESSION.",
    )
    return parser.parse_args()


def determine_year_and_day(args) -> tuple[int, int]:
    today = dt.date.today()

    year = (
        args.year
        if args.year is not None
        else int(os.environ.get("AOC_YEAR", today.year))
    )

    day = args.day if args.day is not None else today.day

    if not (1 <= day <= 25):
        print(f"Day must be between 1 and 25, got {day}.")
        sys.exit(1)

    return year, day


def create_day_directory(base_dir: str, day: int) -> Path:
    day_dir_name = f"{day:02d}"
    day_dir = Path(base_dir).expanduser().resolve() / day_dir_name
    day_dir.mkdir(parents=True, exist_ok=True)
    return day_dir


def download_input(year: int, day: int, session_token: str, dest: Path) -> None:
    if dest.exists():
        print(f"Input file already exists at {dest}, not downloading again.")
        return

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    print(f"Downloading input from {url} ...")

    cookies = {"session": session_token}
    response = requests.get(url, cookies=cookies)

    if response.status_code != 200:
        print(
            f"Failed to download input (status {response.status_code}).\n"
            "Common causes:\n"
            "- Wrong year or day\n"
            "- Day not unlocked yet (AoC puzzle not released)\n"
            "- Invalid or expired session cookie\n"
        )
        sys.exit(1)

    dest.write_text(response.text.rstrip("\n") + "\n", encoding="utf-8")
    print(f"Saved input to {dest}")


def create_test_file(day_dir: Path) -> None:
    test_file = day_dir / "test.txt"
    if not test_file.exists():
        test_file.write_text("", encoding="utf-8")
        print(f"Created empty test file: {test_file}")
    else:
        print(f"test.txt already exists at {test_file}, leaving it as is.")


def create_solution_file(day_dir: Path, year: int, day: int) -> None:
    solution_file = day_dir / "solution.py"
    if solution_file.exists():
        print(f"solution.py already exists at {solution_file}, leaving it as is.")
        return

    template = f"""#!/usr/bin/env python3

def part1(data: list[str]) -> int | str:
    # TODO: implement
    return 0


def part2(data: list[str]) -> int | str:
    # TODO: implement
    return 0


def read_input(filename: str = "input.txt") -> list[str]:
    with open(filename, encoding="utf-8") as f:
        return [line.rstrip("\\n") for line in f]


if __name__ == "__main__":
    import sys

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    data = read_input(filename)

    print("Advent of Code {year} - Day {day:02d}")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
"""

    solution_file.write_text(template, encoding="utf-8")
    try:
        # make it executable on Unix-like systems
        solution_file.chmod(solution_file.stat().st_mode | 0o111)
    except Exception:
        pass

    print(f"Created solution template: {solution_file}")


def create_run_script(day_dir: Path) -> None:
    run_file = day_dir / "run"
    if run_file.exists():
        print(f"run script already exists at {run_file}, leaving it as is.")
        return

    script = """#!/usr/bin/env bash
set -e

# Usage:
#   ./run        # uses input.txt
#   ./run --test # uses test.txt

FILE="input.txt"

if [[ "$1" == "--test" || "$1" == "-t" ]]; then
  FILE="test.txt"
fi

python3 solution.py "$FILE"
"""

    run_file.write_text(script, encoding="utf-8")
    try:
        run_file.chmod(run_file.stat().st_mode | 0o111)
    except Exception:
        pass

    print(f"Created run script: {run_file}")


def main():
    args = parse_args()
    year, day = determine_year_and_day(args)
    session_token = get_session_token(args.session_env)

    print(f"Preparing Advent of Code {year} Day {day:02d}...")

    day_dir = create_day_directory(args.base_dir, day)
    print(f"Using directory: {day_dir}")

    download_input(year, day, session_token, day_dir / "input.txt")
    create_test_file(day_dir)
    create_solution_file(day_dir, year, day)
    create_run_script(day_dir)

    print("Done!")


if __name__ == "__main__":
    main()
