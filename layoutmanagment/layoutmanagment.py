from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QRect, QSize


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("PyQt5 Window")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon("icons/pyicon.png"))

        self.create_layout()

        self.show()


    def create_layout(self):
        grpbox = QGroupBox("What is your favorite operating system?")
        grpbox.setFont(QFont("Times New Roman", 12))

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        # create pushbutton
        btn = QPushButton("Apple", self)
        btn.setIcon(QIcon("icons/apple.png"))
        btn.setIconSize(QSize(40,50))
        hbox.addWidget(btn)

        btn1 = QPushButton("Windows", self)
        btn1.setIcon(QIcon("icons/windows.png"))
        btn1.setIconSize(QSize(40,50))
        hbox.addWidget(btn1)

        btn2 = QPushButton("Linux", self)
        btn2.setIcon(QIcon("icons/linux.png"))
        btn2.setIconSize(QSize(40,50))
        hbox.addWidget(btn2)

        grpbox.setLayout(hbox)

        vbox.addWidget(grpbox)

        self.setLayout(vbox)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())