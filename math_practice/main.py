import json
import sys

import gui
import operations_factory
import plugin_loader
import PyQt5.QtWidgets as pqw


def main() -> None:
    with open("operations.json") as file:
        plugin_data = json.load(file)

    plugin_loader.load_plugins(plugin_data["operation_modules"])

    operations = [operations_factory.create(item) for item in plugin_data["operations"]]
    
    app = pqw.QApplication(sys.argv)
    window = gui.Window(operations)
    app.exec_()


if __name__ == "__main__":
    main()
