import random

import operations_factory


class AddingUpToN:
    def __init__(
        self,
        max_number: int,
        min_number: int = 0,
    ) -> None:
        self.MIN_NUMBER = min_number
        self.MAX_NUMBER = max_number

    def generate_equation(self) -> tuple[str, int]:
        number1 = random.randint(self.MIN_NUMBER, self.MAX_NUMBER)
        number2 = random.randint(self.MIN_NUMBER, self.MAX_NUMBER - number1)
        return f"{number1} + {number2} = ", number1 + number2


def register() -> None:
    operations_factory.register("adding_up_to_n", AddingUpToN)
