from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QPushButton
import sys
from PyQt5.QtGui import QIcon
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("PyQt5 LCD Number")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon("icons/pyicon.png"))

        self.lcd_number()
      

        self.show()


    def lcd_number(self):
        vbox = QVBoxLayout()
        self.lcd = QLCDNumber()
        self.lcd.setStyleSheet('background-color:red')
        vbox.addWidget(self.lcd)

        btn = QPushButton("Random Number Generator")
        btn.setStyleSheet('background-color:green')
        btn.clicked.connect(self.lcd_handler)
        vbox.addWidget(btn)

        self.setLayout(vbox)


    def lcd_handler(self):
        random = randint(1,200)
        self.lcd.display(random)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())