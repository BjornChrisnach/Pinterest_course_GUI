from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox ,QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("PyQt5 CheckBox")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon("icons/pyicon.png"))

        self.create_checkbox()

        self.show()

    def create_checkbox(self):
        grpbox = QGroupBox("What Is Your Favorite Operating System?")
        grpbox.setFont(QFont("Times New Roman", 12))
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        self.check1 = QCheckBox("Apple")
        self.check1.setIcon(QIcon("icons/apple.png"))
        self.check1.setIconSize(QSize(40, 40))
        self.check1.setFont(QFont("Times New Roman", 13))
        hbox.addWidget(self.check1)
        self.check1.toggled.connect(self.on_toggled)

        self.check2 = QCheckBox("Windows")
        self.check2.setIcon(QIcon("icons/windows.png"))
        self.check2.setIconSize(QSize(40, 40))
        self.check2.setFont(QFont("Times New Roman", 13))
        hbox.addWidget(self.check2)
        self.check2.toggled.connect(self.on_toggled)

        self.check3 = QCheckBox("Linux")
        self.check3.setIcon(QIcon("icons/linux.png"))
        self.check3.setIconSize(QSize(40, 40))
        self.check3.setFont(QFont("Times New Roman", 13))
        hbox.addWidget(self.check3)
        self.check3.toggled.connect(self.on_toggled)
        

        self.label = QLabel("Hello ", self)
        self.label.setFont(QFont("Sanserif", 15))
        vbox.addWidget(self.label)

        grpbox.setLayout(hbox)
        vbox.addWidget(grpbox)

        self.setLayout(vbox)


    def on_toggled(self):
        if self.check1.isChecked():
            self.label.setText("You have checked: {} ".format(self.check1.text()))

        if self.check2.isChecked():
            self.label.setText("You have checked: {} ".format(self.check2.text()))

        if self.check3.isChecked():
            self.label.setText("You have checked: {} ".format(self.check3.text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())