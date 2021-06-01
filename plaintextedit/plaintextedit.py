from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPlainTextEdit
import sys
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("PyQt5 PlainTextEdit")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon("icons/pyicon.png"))

        vbox = QVBoxLayout()
        plain_textedit = QPlainTextEdit()
        plain_textedit.setPlaceholderText("This is a placeholder")
        # plain_textedit.setReadOnly(True)

        text = "This is appended text"
        plain_textedit.appendPlainText(text)

        vbox.addWidget(plain_textedit)

        self.setLayout(vbox)

        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())