from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QVBoxLayout
import sys
from PyQt5.QtGui import QIcon, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.create_ui()

    def create_ui(self):
        self.setWindowTitle("PyQt5 Combobox")
        self.setGeometry(100, 100, 600, 300)
        self.setWindowIcon(QIcon("comboboxex/pyicon.png"))

        self.create_combo()

        self.show()


    def create_combo(self):
        vbox = QVBoxLayout()

        self.combobox = QComboBox()
        self.combobox.addItem('Java')
        self.combobox.addItem('C++')
        self.combobox.addItem('Python')
        self.combobox.addItem('Kotlin')
        self.combobox.addItem('C#')
        self.combobox.currentTextChanged.connect(self.combo_changed)


        self.label = QLabel()
        self.label.setFont(QFont("Times New Roman", 14))

        vbox.addWidget(self.combobox)
        vbox.addWidget(self.label)

        self.setLayout(vbox)


    def combo_changed(self):
        text = self.combobox.currentText()
        self.label.setText("You have selected {}".format(text))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())