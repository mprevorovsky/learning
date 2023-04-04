import random
from typing import Callable

from operations_factory import Operation


def generate_equation(operations: list[Operation]) -> tuple[str, int]:
    return random.choice(operations).generate_equation()

