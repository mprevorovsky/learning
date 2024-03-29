import random
import sys

import PyQt5.QtWidgets as pqw
import PyQt5.uic as pqu

TASKS = 7
MIN_NUMBER = 0
MAX_NUMBER = 20
SYMBOL_WRONG = "🐷"
SYMBOL_OK = "💙"  # "🍭"


class Window(pqw.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.task_counter = 1
        self.ok_counter = 0
        self.wrong_counter = 0
        self.score = ""
        self.equation, self.result = self._generate_equation()

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

    def _generate_equation(self) -> tuple[str, int]:
        operation = random.choice(["+", "-"])
        if operation == "+":
            number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
            number2 = random.randint(MIN_NUMBER, MAX_NUMBER - number1)
            result = number1 + number2
        elif operation == "-":
            number1 = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number1 > 10:
                number2 = random.randint(MIN_NUMBER, number1 - 10)
            else:
                number2 = random.randint(MIN_NUMBER, number1)
            result = number1 - number2
        return (f"{number1} {operation} {number2} =", result)

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


def main() -> None:
    app = pqw.QApplication(sys.argv)
    window = Window()
    app.exec_()


if __name__ == "__main__":
    main()
