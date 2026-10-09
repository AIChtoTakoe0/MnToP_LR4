import logging
from functools import wraps

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(
            "Вызов %s: args=%r, kwargs=%r",
            func.__name__, args, kwargs
        )
        try:
            result = func(*args, **kwargs)
            logging.info("%s вернула: %r", func.__name__, result)
            return result
        except Exception:
            logging.exception("Ошибка в функции %s", func.__name__)
            raise

    return wrapper


@log_call
def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(2, 3))
