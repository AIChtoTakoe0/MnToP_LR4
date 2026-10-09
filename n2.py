import random
from typing import Iterator


def random_numbers(start: int, end: int, count: int) -> Iterator[int]:
    for _ in range(count):
        yield random.randint(start, end)


if __name__ == "__main__":
    for number in random_numbers(1, 10, 5):
        print(number)
