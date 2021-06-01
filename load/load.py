from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("UI/mainwindow.ui", self)

        self.textedit = self.findChild(QTextEdit, "textEdit")
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.clickedBtn)

        self.show()

    def clickedBtn(self):
        self.textedit.setPlainText("Please subscribe to my channel and like the video")


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()