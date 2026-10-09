class Countdown:
    """Итератор обратного отсчёта от start до 1."""

    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


if __name__ == "__main__":
    for number in Countdown(5):
        print(number)
