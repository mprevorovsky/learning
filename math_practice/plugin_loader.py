import importlib


class ModuleInterface:
    @staticmethod
    def register() -> None:
        ...


def import_module(name: str) -> ModuleInterface:
    return importlib.import_module(name)  # type: ignore


def load_plugins(plugins: list[str]) -> None:
    for plugin_file in plugins:
        plugin = import_module(plugin_file)
        plugin.register()
