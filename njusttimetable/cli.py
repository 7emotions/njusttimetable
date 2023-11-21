"""Console script for njusttimetable."""

import fire


def help() -> None:
    print("njusttimetable")
    print("=" * len("njusttimetable"))
    print("Help you obtain your timetable")


def main() -> None:
    fire.Fire({"help": help})


if __name__ == "__main__":
    main()  # pragma: no cover
