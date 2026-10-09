import random
from itertools import islice
from typing import Iterator


def infinite_random(start: int, end: int) -> Iterator[int]:
    """Бесконечный генератор случайных целых чисел в диапазоне [start, end]."""
    while True:
        yield random.randint(start, end)


if __name__ == "__main__":
    generator = infinite_random(1, 100)
    for number in islice(generator, 10):
        print(number)
