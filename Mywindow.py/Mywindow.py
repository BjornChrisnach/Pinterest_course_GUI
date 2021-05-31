from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QRect, QSize


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("PyQt5 Window")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon("icons/pyicon.png"))

        self.create_widget()

        self.show()

    def create_widget(self):
        # create pushbutton
        self.btn = QPushButton("Click Me", self)
        self.btn.setGeometry(QRect(50,50,100,50))
        self.btn.setIcon(QIcon("icons/pyicon.png"))
        self.btn.setIconSize(QSize(40,50))
        self.btn.setToolTip("<h2>I am a button</h2>")

        self.btn.clicked.connect(self.btn_clicked)

        # create my label
        self.label = QLabel("I am a label", self)
        self.label.setFont(QFont("Times New Roman", 15))
        self.label.setStyleSheet('color:green')
        self.label.setGeometry(QRect(120,120,200,200))



    def btn_clicked(self):
        self.label.setText("Button Is clicked")
        self.label.setStyleSheet('color:red')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())