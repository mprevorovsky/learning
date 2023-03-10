from typing import Any, Callable, Protocol


class Operation(Protocol):
    def generate_equation(self) -> tuple[str, int]:
        ...


equation_creation_functions: dict[str, Callable[..., Operation]] = {}


def register(operation_name: str, creator_function: Callable[..., Operation]) -> None:
    equation_creation_functions[operation_name] = creator_function


def unregister(operation_name: str) -> None:
    equation_creation_functions.pop(operation_name, None)


def create(arguments: dict[str, Any]) -> Operation:
    arguments_copy = arguments.copy()
    operation_name = arguments_copy.pop("name")
    creator_function = equation_creation_functions[operation_name]
    return creator_function(**arguments_copy)
