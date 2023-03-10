import random

import operations_factory


class SubtractionUpTo20:
    def __init__(
        self,
        max_number: int = 20,
        min_number: int = 0,
        cross_ten: bool = False,
    ) -> None:
        self.MIN_NUMBER = min_number
        self.MAX_NUMBER = max_number
        self.cross_ten = cross_ten

    def generate_equation(self) -> tuple[str, int]:
        number1 = random.randint(self.MIN_NUMBER, self.MAX_NUMBER)
        if self.cross_ten:
            number2 = random.randint(self.MIN_NUMBER, number1 - 10)
        else:
            number2 = random.randint(self.MIN_NUMBER, number1)
        return f"{number1} - {number2} = ", number1 - number2


def register() -> None:
    operations_factory.register("subtraction_up_to_20", SubtractionUpTo20)
