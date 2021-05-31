from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
import sys
from PyQt5.QtGui import QIcon, QFont


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("PyQt5 TextEdit")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon("icons/pyicon.png"))

        self.create_text()

        self.show()


    def create_text(self):
        text = QTextEdit(self)
        text.setFont(QFont("Times New Roman", 15))
        self.setCentralWidget(text)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())