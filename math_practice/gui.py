from typing import Callable

import PyQt5.QtWidgets as pqw
import PyQt5.uic as pqu
from operations_factory import Operation

SYMBOL_WRONG = "🐷"
SYMBOL_OK = "💙"  # "🍭"
TASKS = 7


class Window(pqw.QWidget):
    def __init__(self, operations: dict[str, Callable[..., Operation]]) -> None:
        super().__init__()
        self.task_counter = 1
        self.ok_counter = 0
        self.wrong_counter = 0
        self.score = ""
        self.operations = operations
        self.equation, self.result = self.operations._generate_equation()

        self._setup()
        self.label_equation.setText(self.equation)
        self.label_score.setText(self.score)
        self.label_overall_score.setText(
            f"{SYMBOL_OK} {self.ok_counter}  {SYMBOL_WRONG} {self.wrong_counter}"
        )

    def _setup(self) -> None:
        pqu.loadUi("math_practice.ui", self)
        self.label_equation = self.findChild(pqw.QLabel, "label_equation")
        self.label_score = self.findChild(pqw.QLabel, "label_score")
        self.label_overall_score = self.findChild(pqw.QLabel, "label_overall_score")
        self.lineEdit_result = self.findChild(pqw.QLineEdit, "lineEdit_result")
        self.pushButton_again = self.findChild(pqw.QPushButton, "pushButton_again")

        self.setWindowTitle("Matematika")
        self.lineEdit_result.returnPressed.connect(self._evaluate_answer)
        self.pushButton_again.clicked.connect(self._reset)
        self.showMaximized()

    def _evaluate_answer(self) -> None:
        if int(self.lineEdit_result.text()) == self.result:
            self.score = f"{self.score}{SYMBOL_OK}"
            self.ok_counter += 1
        else:
            self.score = f"{self.score}{SYMBOL_WRONG}"
            self.wrong_counter += 1

        if self.task_counter < TASKS:
            self.equation, self.result = self._generate_equation()
            self.label_equation.setText(self.equation)
            self.task_counter += 1
        else:
            self.label_equation.setText("Hotovo!")
            self.lineEdit_result.setEnabled(False)
            self.pushButton_again.setEnabled(True)
            self.pushButton_again.setFocus()

        self.label_score.setText(self.score)
        self.lineEdit_result.setText("")
        self.label_overall_score.setText(
            f"{SYMBOL_OK} {self.ok_counter}  {SYMBOL_WRONG} {self.wrong_counter}"
        )

    def _reset(self) -> None:
        self.task_counter = 1
        self.score = ""
        self.equation, self.result = self._generate_equation()
        self.label_equation.setText(self.equation)
        self.label_score.setText(self.score)
        self.lineEdit_result.setEnabled(True)
        self.pushButton_again.setEnabled(False)
