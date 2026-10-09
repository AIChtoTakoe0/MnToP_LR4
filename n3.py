from functools import reduce
from typing import Iterable, Union

Number = Union[int, float]


def sum_reduce(numbers: Iterable[Number]) -> Number:
    return reduce(lambda x, y: x + y, numbers, 0)


if __name__ == "__main__":
    print(sum_reduce([1, 2, 3, 4, 5]))  # 15
