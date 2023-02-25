import random
from typing import Protocol


class Operation(Protocol):
    def generate_equation(self) -> tuple[str, int]:
        ...


class OperationsList:
    def __init__(self) -> None:
        self.operations = []

    def register_operation(self, operation: Operation) -> None:
        self.operations.append(operation)


class AddingUpToN(Operation):
    def __init__(
        self,
        operations_list: OperationsList,
        max_number: int,
        tasks: int = 7,
        min_number: int = 0,
    ) -> None:
        self.TASKS = tasks
        self.MIN_NUMBER = min_number
        self.MAX_NUMBER = max_number
        operations_list.register_operation(self)

    def generate_equation(self) -> tuple[str, int]:
        number1 = random.randint(self.MIN_NUMBER, self.MAX_NUMBER)
        number2 = random.randint(self.MIN_NUMBER, self.MAX_NUMBER - number1)
        return f"{number1} + {number2} = ", number1 + number2


class SubtractionUpTo20(Operation):
    def __init__(
        self,
        operations_list: OperationsList,
        max_number: int,
        tasks: int = 7,
        min_number: int = 0,
        cross_ten: bool = False,
    ) -> None:
        self.TASKS = tasks
        self.MIN_NUMBER = min_number
        self.MAX_NUMBER = max_number
        self.cross_ten = cross_ten
        operations_list.register_operation(self)

    def generate_equation(self) -> tuple[str, int]:
        number1 = random.randint(self.MIN_NUMBER, self.MAX_NUMBER)
        if self.cross_ten:
            number2 = random.randint(self.MIN_NUMBER, number1 - 10)
        else:
            number2 = random.randint(self.MIN_NUMBER, number1)
        return f"{number1} - {number2} = ", number1 - number2
