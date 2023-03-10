from typing import Any, Callable, Protocol


class Operation(Protocol):
    def generate_equation(self) -> tuple[str, int]:
        ...


equation_creation_functions: dict[str, Callable[..., Operation]] = {}


def register(operation_type: str, creator_function: Callable[..., Operation]) -> None:
    equation_creation_functions[operation_type] = creator_function


def unregister(operation_type: str) -> None:
    equation_creation_functions.pop(operation_type, None)


def create(arguments: dict[str, Any]) -> Operation:
    arguments_copy = arguments.copy()
    operation_type = arguments_copy.pop("operation_type")
    creator_function = equation_creation_functions[operation_type]
    return creator_function(**arguments_copy)
