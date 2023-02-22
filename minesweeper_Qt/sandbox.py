import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Minesweeper")
        self.setLayout(qtw.QVBoxLayout())
        greeting = qtw.QLabel("Welcome to the Minesweeper game!")
        self.layout().addWidget(greeting)
        self.show()


app = qtw.QApplication([])
window = MainWindow()

app.exec_()
